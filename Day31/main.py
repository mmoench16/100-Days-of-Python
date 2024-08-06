from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
card_back_img = PhotoImage(file="Day31/images/card_back.png")
card_front_img = PhotoImage(file="Day31/images/card_front.png")
right_img = PhotoImage(file="Day31/images/right.png")
wrong_img = PhotoImage(file="Day31/images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526)
canvas.create_image(400,263, image=card_front_img)
canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
correct_btn.grid(row=1,column=1)

wrong_btn = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_btn.grid(row=1,column=0)

window.mainloop()