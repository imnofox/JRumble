from tkinter import *

class Highscores:
    def __init__(self, controller, entry_mode=False, score=0):
        self.title = "Highscores"
        self.window = Tk()
        self.window.title(self.title)
        
        self.controller = controller
        
        self.entry_mode = entry_mode
        self.score = score
        
        self.draw_layout()
        
    def draw_layout(self):        
        self.listbox = Listbox(self.window, width=50)
        self.listbox.grid(row=0, column=0, columnspan=3)
        
        n = 1
        print(self.controller.scores)
        for score in self.controller.scores:
            # Also add left padding zeroes to score
            self.listbox.insert(n, '{0:02d}'.format(score['score']) + ' ' + score['name'])
            n += 1
        
        if self.entry_mode:
            self.text_entry = Entry(self.window)
            self.text_entry.insert(END, "Enter username")
            self.text_entry.grid(row=2, column=0, columnspan=2, sticky='WE')
            
            self.submit_button = Button(self.window, text="Submit", command=self.save_score)
            self.submit_button.grid(row=2, column=2, sticky='WE')
        
        else:
            self.close_button = Button(self.window, text="Close", command=self.quit)
            self.close_button.grid(row=1, column=0, columnspan=3)
            
    def save_score(self):
        username = self.text_entry.get()
        if username.isalnum():
            self.controller.add_highscore(self.score, username)
            self.quit()
        else:
            pass
        
    def quit(self):
        self.window.destroy()