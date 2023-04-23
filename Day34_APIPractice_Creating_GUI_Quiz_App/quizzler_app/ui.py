from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300,
                             height=250,
                             bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Text here",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        """
        By giving self, it turns this into a property which can be accessed anywhere in the class.
        """
        correct_img = PhotoImage(file="../quizzler_app/images/true.png")
        self.true_button = Button(image=correct_img,
                                  highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        wrong_img = PhotoImage(file="../quizzler_app/images/false.png")
        self.wrong_button = Button(image=wrong_img,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        # Score label
        self.score_label = Label(text="Score:",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text="End of the quiz!")
            # Disable the buttons once quiz is finished.
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
