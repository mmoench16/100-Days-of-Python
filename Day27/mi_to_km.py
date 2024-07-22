from tkinter import *

def convert():
    dist = float(input.get())
    dist *= 1.60934
    dist = str(round(dist,2))
    dist_label.config(text=dist)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)

dist_label = Label(text="0")
dist_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Buttons
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

# Needs to be at the very end of the program
window.mainloop()