from tkinter import *

'''
|  ||
|| |_
'''

class Loss(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        self.configure(bg="#DB4545")
        
        self.score =0
        self.is_highscore = False
        
        self.draw_layout()
        
    def draw_layout(self):
        print(self.is_highscore)
        self.title_txt = StringVar()
        self.title = Label(self, textvariable=self.title_txt, font=("Comic Sans MS", 60, 'bold'), bg="#DB4545", fg="#ffffff")
        self.title.pack(padx=5)
        
        self.emoji_sad = PhotoImage(file="images/sad.gif")
        self.emoji_happy = PhotoImage(file="images/happy.gif")
        self.emoji_image = Label(self, image=self.emoji_sad, bg="#DB4545")
        self.emoji_image.pack()
        
        self.score_txt = StringVar()
        self.score = Label(self, textvariable=self.score_txt, font=("Comic Sans MS", 60, 'bold'), bg="#DB4545", fg="#ffffff")
        self.score.pack(padx=5)
        
        self.button = Button(self, text="Main Menu", width=15, bg="#FFE6CC", pady=10, font=("Comic Sans MS", 12), command=lambda: self.controller.show_frame("MainMenu"))
        self.button.pack(pady=2)
        
    def start(self, score=None, is_highscore=False, *args, **kwargs):
        self.score = score
        self.is_highscore = is_highscore
        
        self.score_txt.set(str(self.score))
        
        if self.is_highscore:
            self.title_txt.set("Highscore!")
            self.emoji_image.config(image=self.emoji_happy)
        else:
            self.title_txt.set("Gameover!")
            self.emoji_image.config(image=self.sad)
    