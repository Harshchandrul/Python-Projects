from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz Application")
        self.window.config(bg=THEME_COLOR, pady=40, padx=40)

        # TODO creating score_label
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("JetBrains Mono", 12, "normal"),
                                 bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # TODO creating canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(150, 125, text="HELLO WORLD", fill=THEME_COLOR,
                                                     font=('JetBrains Mono', 16, "italic"), width=280)

        self.get_next_question()  # Calling the function to display q_text

        # TODO creating buttons
        false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=false_img, borderwidth=0, command=self.false_pressed)

        self.false_btn.grid(column=0, row=2)
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, borderwidth=0, command=self.true_pressed)

        self.true_btn.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")

    def true_pressed(self):
        is_correct = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        print("Give feedback executed")
        if is_correct:
            self.canvas.config(bg="green")
            print("Color changed")
        else:
            self.canvas.config(bg="red")
            print("Color changed")
        self.window.after(500, self.get_next_question)
