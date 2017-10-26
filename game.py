from tkinter import *
import re
from random import randrange, choice
from datetime import datetime

class Game(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        
        self.SUCCESS_POINTS = 25
        self.SCORE_DECREASE_SPEED = 500
        
        self.timer = None
        
        self.reset_vars()
        self.draw_layout()
        self.reset_hearts()
        
    def reset_vars(self, difficulty=1):
        self.difficulty = difficulty
        self.lives = 3
        self.score = 100
        self.equation_filled = False
        self.button_mode = 0 # 0 for Go!, 1 for Next
        
    def draw_layout(self):
        self.frame = Frame(self)
        self.frame.pack()
        
        # Create scorebar frame
        self.scorebar = Frame(self.frame, bg="#FFE6CC", width=1000)
        self.scorebar.grid(sticky="WE")
    
        # Create the score label (sits left)
        self.score_label_text = StringVar()
        self.score_label_text.set(str(self.score))
        self.score_label = Label(self.scorebar, textvariable=self.score_label_text, font=("Comic Sans MS", 15, 'bold'), bg="#FFE6CC", width=6)
        self.score_label.grid(row=0, column=0, sticky="W")
        
        # Create the quit button (sits centre)
        self.quit_button = Button(self.scorebar, text="Quit", width=15, bg="#F8CECC", pady=2, font=("Comic Sans MS", 10, 'bold'), command=lambda: self.controller.show_frame("MainMenu"))
        self.quit_button.grid(row=0, column=1)
        
        # Create the hearts frame (sits right)
        self.hearts_frame = Frame(self.scorebar, width=3)
        self.hearts_frame.grid(row=0, column=2, sticky="E")
        
        # Create the red heart
        self.red_heart = PhotoImage(file="images/red.gif")
        self.grey_heart = PhotoImage(file="images/grey.gif")
        
        # Create each heart
        self.hearts = []
        self.hearts.append(Label(self.hearts_frame, image=self.red_heart, bg="#FFE6CC"))
        self.hearts[0].image = self.red_heart
        self.hearts[0].grid(row=0, column=0)
        
        self.hearts.append(Label(self.hearts_frame, image=self.red_heart, bg="#FFE6CC"))
        self.hearts[1].image = self.red_heart
        self.hearts[1].grid(row=0, column=1)
        
        self.hearts.append(Label(self.hearts_frame, image=self.red_heart, bg="#FFE6CC"))
        self.hearts[2].image = self.red_heart
        self.hearts[2].grid(row=0, column=2)
        
        # Ensure columns in scorebar sit correctly
        Grid.columnconfigure(self.scorebar, 0, weight=1)
        Grid.columnconfigure(self.scorebar, 2, weight=1)
        
        # Create the button grid FRAME
        self.grid_frame = Frame(self.frame, width=600, height=300, bg="#27ab87")
        self.grid_frame.grid(row=2, sticky="WE", padx=10, pady=10)
        
        # Create the frame to hold the bottom stuff
        self.equation_frame = Frame(self.frame, padx=20, pady=10)
        self.equation_frame.grid(row="3", sticky="WE")
        
        # Create the equation text label
        self.equation_label_text = StringVar()
        self.equation_label = Label(self.equation_frame, textvariable=self.equation_label_text, font=("Comic Sans MS", 25, 'bold'))
        self.equation_label.pack()
        
        # And create the next button
        self.next_button = Button(self.equation_frame, text="Go!", state=DISABLED, bg="#FFE6CC", width=15, pady=2, font=("Comic Sans MS", 10, 'bold'), command=self.main_button)
        self.next_button.pack()
        
        # And the correct/wrong ticks
        self.pixel = PhotoImage(file="images/pixel.gif")
        self.tick = PhotoImage(file="images/correct.gif")
        self.cross = PhotoImage(file="images/wrong.gif")
        self.status_image = Label(self.equation_frame, image=self.pixel)
        self.status_image.pack(pady=10)
        
    # Reset the hearts on display
    def reset_hearts(self):
        for h in self.hearts:
            h.configure(image=self.red_heart)
        
    # Generate an equation
    def generate_equation(self):
        if self.difficulty == 1:
            operators = ['+', '-']
        elif self.difficulty in [2, 3]:
            operators = ['+', '-', '*', '/']
            
        def gen_equation_and_result():        
            number_of_operators = randrange(1, 4)
            number_of_numbers = number_of_operators + 1
        
            equation = ""
        
            # Add operators
            num_operators = 0
            used_hard_operator = False
            while num_operators < number_of_operators:
                operator = choice(operators)
                # Prevent making equations TOO hard for medium
                if operator in ['*', '/'] and self.difficulty == 2:
                    if not used_hard_operator:
                        equation += operator
                        number_of_operators
                        used_hard_operator = True
                else:
                    equation += operator
                    num_operators += 1
                        
            # Add spaces
            equation = list(equation)
            equation = '?' + '?'.join(equation) + '?'
        
            # Add some numbers
            def cb(o):
                return str(randrange(1, 10))
            final_equation = re.sub(r'\?', cb, equation)
        
            # Find the answer
            result = eval(final_equation)
        
            return result, equation
        
        result = -1
        equation = ""
        while result < 0:
            result, equation = gen_equation_and_result()
            
        return result, equation
    
    # Disable a button
    def disable_button(self, x, y):
        self.buttons[y][x].configure(state=DISABLED, bg="#939393")
    
    # Generate the grid AFRESH    
    def fill_grid(self):
        for child in self.grid_frame.winfo_children():
            child.destroy()
            
        self.buttons = []
        
        # Button press event
        def b_press(n, x, y):
            #print("{0} at {1}, {2} pressed".format(n, x , y))
            if (not self.equation_filled):
                self.update_equation(n)
                self.disable_button(x, y)
        
        # 7 rows    
        for y in range(0, 7):
            self.buttons.append([])
            # 17 columns
            for x in range(0, 17):
                c = randrange(1, 10)
                b = Button(self.grid_frame, text=str(c), padx=5, bg="#FFE6CC", font=("Comic Sans MS", 10, 'bold'), command=lambda x=x, y=y, c=c: b_press(c, x, y))
                b.grid(row=y, column=x, padx=2, pady=2)
                self.buttons[y].append(b)

    # Initially fill + generate the initial empty equation
    def fill_equation(self):
        self.result, self.equation = self.generate_equation()
        self.equation_label_text.set(self.equation + '=' + str(self.result))
        
    # Update equation text, filling in the next number
    def update_equation(self, n):
        self.equation = self.equation.replace('?', str(n), 1)
        if (self.equation.count('?') == 0):
            self.next_button.configure(state=NORMAL)
            self.equation_filled = True
        self.equation_label_text.set(self.equation + '=' + str(self.result))
    
    # Handle the main button's two functions
    def main_button(self):
        if self.button_mode == 1:
            self.next_round()
        else:
            self.check_answer()
    
    # Check their answer
    def check_answer(self):
        workable_equation = self.equation + '==' + str(self.result)
        if eval(workable_equation):
            self.score += self.SUCCESS_POINTS
            self.score_label_text.set(str(self.score))
            self.status_image.configure(image=self.tick)
        else:
            self.remove_life()
            self.status_image.configure(image=self.cross)
        self.button_mode = 1
        self.next_button.configure(text="Next Question")
    
    # Remove a life        
    def remove_life(self):
        if self.lives >= 1:
            self.lives -= 1
            self.hearts[2 - self.lives].configure(image=self.grey_heart)
    
        if self.lives < 1:
            self.do_loss()
    
    # Stop the timer
    def stop_timer(self):
        if self.timer:
            self.after_cancel(self.timer)
    
    # Run the timer
    def timer_score(self):
        self.score -= 1
        self.score_label_text.set(str(self.score))
        
        self.timer = self.after(self.SCORE_DECREASE_SPEED, self.timer_score)
        
        if self.score < 1:
            self.do_loss()
    
    # Do a round    
    def next_round(self):
        self.fill_grid()
        self.fill_equation()
        
        self.equation_filled = False
        self.status_image.configure(image=self.pixel)
        self.button_mode = 0
        self.next_button.configure(text="Go!", state=DISABLED)
        
    def do_loss(self):
        self.stop_timer()
        is_highscore = self.controller.is_highscore(self.score)
        if is_highscore:
            self.controller.show_highscores(entry_mode=True, score=self.score)
        self.controller.show_frame("Loss", score=self.score, is_highscore=is_highscore)
        
    def start(self, difficulty=1):
        self.stop_timer()
        self.reset_vars(difficulty)
        self.reset_hearts
        print("Diff: " + str(difficulty))
        
        # Start the timer
        self.timer_score()
        
        self.next_round()
        