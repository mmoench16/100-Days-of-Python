from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas & Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="Day29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_btn = Button(text="Generate Password")
gen_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()