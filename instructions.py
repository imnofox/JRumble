from tkinter import *

class Instructions:
    def __init__(self):
        self.title = "Instructions"
        self.window = Tk()
        self.window.title(self.title)
        self.window.resizable(False, False)
        
        self.create()
        
    def create(self):
        file = open("texts/instructions.txt", 'r')
        
        self.frame = LabelFrame(self.window, text=self.title, padx=5, pady=5)
        self.frame.pack()
        
        text = Label(self.frame, text=file.read(), wraplength=400, justify=LEFT)
        text.pack()
        
        file.close()
        
        button = Button(self.window, text="Close", command=self.window.destroy)
        button.pack()
        
    def quit(self):
        self.window.destroy()