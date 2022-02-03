from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(width=300,height=250,highlightthickness=0,bg='white')
        self.canvas.grid(column=0,row=1,columnspan = 2, pady = 50)
            # Canvas text
        self.canvas_text = self.canvas.create_text(150, 125, width = 280, text='Text', font=('Ariel', 20, 'italic'),fill='black')


        # Labels
        self.score_label = Label(text=f'Score : {self.quiz.score}', bg = THEME_COLOR, fg='white', font = ('Arial',13, 'bold'))
        self.score_label.grid(row=0,column=1)

        # Buttons
            # True button
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(row = 2,column=0)
            # False button
        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(row = 2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text = q_text)
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.config(bg='white')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

            self.canvas.itemconfig(self.canvas_text, text=f"Score {self.quiz.score}/10")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


