from tkinter import *

class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        self.title = "JungleRumble"
        self.draw_layout()
    
    def draw_layout(self):
        self.menu = Frame(self, bg="#27ab87")
        self.menu.pack(side="top", fill="both", expand=True)
        
        self.title = Label(self.menu, text=self.title, font=("Comic Sans MS", 60, 'bold'), bg="#27ab87")
        self.title.pack(padx=5)
        
        pad = 2
        font = ("Comic Sans MS", 12)
        
        self.button_easy = Button(self.menu, text="Easy", width=15, bg="#FFE6CC", pady=pad, font=font, command=lambda: self.start_game(1))
        self.button_easy.pack(pady=2)
        
        self.button_medium = Button(self.menu, text="Medium", width=15, bg="#FFE6CC", pady=pad, font=font, command=lambda: self.start_game(2))
        self.button_medium.pack(pady=2)
        
        self.button_hard = Button(self.menu, text="Hard", width=15, bg="#FFE6CC", pady=pad, font=font, command=lambda: self.start_game(3))
        self.button_hard.pack(pady=2)
        
        self.button_hs = Button(self.menu, text="High Scores", width=15, bg="#D5E8D4", pady=pad, font=font, command=self.controller.show_highscores)
        self.button_hs.pack(pady=2)
        
        self.button_ins = Button(self.menu, text="Instructions", width=15, bg="#D5E8D4", pady=pad, font=font, command=self.controller.show_instructions)
        self.button_ins.pack(pady=2)
        
        self.button_quit = Button(self.menu, text="Quit", width=15, bg="#F8CECC", pady=pad, font=font, command=self.quit)
        self.button_quit.pack(pady=2)
        
    def start_game(self, difficulty):
        self.controller.show_frame("Game", difficulty=difficulty)
        pass
    
    def start(self, *args, **kwargs):
        pass
        