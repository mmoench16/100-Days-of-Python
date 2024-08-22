from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.minsize(width=500, height=300)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(
            150, 
            125, 
            text="Placeholder", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
            )
        self.canvas.config(highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        # Buttons
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.true_btn.grid(row=2,column=0)

        self.false_btn = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.false_btn.grid(row=2,column=1)

        # Labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0) 

        self.window.mainloop()
