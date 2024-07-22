from tkinter import *

def button_clicked():
    print("I got clicked.")
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI program.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
# my_label.pack()
my_label.grid(column=0, row=0)

# Buttons
button = Button(text="Click Me", command=button_clicked)
button_2 = Button(text="New Button")

# button.pack()
button.grid(column=1, row=1)
button_2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# Needs to be at the very end of the program
window.mainloop()