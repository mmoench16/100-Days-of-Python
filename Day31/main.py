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
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400,263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Labels

window.mainloop()