from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# Load data
to_learn = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

# Generate new random word
def next_card():
    current_card = random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(language, text=f"French")
    canvas.itemconfig(word, text=f"{current_card["French"]}")


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526)
canvas.create_image(400,263, image=card_front_img)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
correct_btn.grid(row=1,column=1)

wrong_btn = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1,column=0)

next_card()

window.mainloop()