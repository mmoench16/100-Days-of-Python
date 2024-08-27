from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.minsize(width=500, height=300)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Placeholder", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
            )
        self.canvas.config(highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        # Buttons
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_btn.grid(row=2,column=0)

        self.false_btn = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.false_pressed)
        self.false_btn.grid(row=2,column=1)

        # Labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0) 

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

