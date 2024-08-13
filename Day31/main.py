from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# Load data
try:
    to_learn = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except:
    to_learn = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

current_card = {}

# Generate new random word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(language, text=f"French", fill="black")
    canvas.itemconfig(word, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

# Flip the card
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language, fill = "white", text="English")
    canvas.itemconfig(word, fill = "white", text=f"{current_card["English"]}")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Load images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400,263, image=card_front_img)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
correct_btn.grid(row=1,column=1)

wrong_btn = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1,column=0)

next_card()

window.mainloop()