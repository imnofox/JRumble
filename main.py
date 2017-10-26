from tkinter import *
from menu import *
from game import *
from loss import *
from instructions import *
from highscores import *
from operator import itemgetter

class JungleRumble(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.scores = []
        self.load_highscores()
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.instructions = None
        self.highscores = None
        
        self.frames = {}
        # Cycle through frames, making them exist
        for F in (MainMenu, Game, Loss):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="NWSE")
            self.frames[page_name] = frame
            
        self.show_frame("MainMenu")
        
    def show_frame(self, page_name, **kwargs):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.start(**kwargs)
        frame.tkraise()
        
    def load_highscores(self):
        with open("texts/highscores.txt", 'r') as f:
            for line in f:self.scores.append({'name': line.split(':')[0], 'score': int(line.split(':')[1])})
        
    def is_highscore(self, user_score=0):
        for score in self.scores:
            if score['score'] < user_score:
                print(str(user_score) + " is highscore")
                return True
        return False
    
    def add_highscore(self, score, name):
        self.scores = self.scores[:-1]
        self.scores.append({
            'name': name,
            'score': score
        })
        self.scores = sorted(self.scores, key=itemgetter('score'), reverse=True)
        self.save_highscores()
        
    def save_highscores(self):
        with open("texts/highscores.txt", 'w') as scores_file:
            for score in self.scores:
                scores_file.write(score['name'] + ':' + str(score['score']) + '\n')
    
    def show_highscores(self, entry_mode=False, score=0):
        self.highscores = Highscores(self, entry_mode=entry_mode, score=score)

    def show_instructions(self):
        self.instructions = Instructions()
        
    def quit_windows(self):
        self.quit()

if __name__ == '__main__':    
    game = JungleRumble()
    game.title("JungleRumble")
    game.geometry("564x570")
    game.resizable(False, False)
    game.protocol("WM_DELETE_WINDOW", game.quit_windows)
    game.mainloop()