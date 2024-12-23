from flask import Flask
import random

random_number = random.randint(0, 9)
print(f"Random number: {random_number}")

app = Flask(__name__)

# Decorator functions ⬇️
@app.route("/")
def home():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
        "<img height='400' \
        style='display: block; margin-left: auto; margin-right: auto;' \
        src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzFmNXNnMjRucGEzOXY0YmlhenR3bmtoYTFyOHI5MW1xOG4weTQzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif'>"

@app.route("/<int:number>")
def number(number):
    if not isinstance(number, int):
        return "<h1>Invalid input.</h1>"

    too_high = "<h1 style='text-align:center; color:purple;'>Too high, try again.</h1>" \
        "<img height='400' \
        style='display: block; margin-left: auto; margin-right: auto;' \
        src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    too_low = "<h1 style='text-align:center; color:red;'>Too low, try again.</h1>" \
        "<img height='400' \
        style='display: block; margin-left: auto; margin-right: auto;' \
        src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    just_right = "<h1 style='text-align:center; color:green;'>Correct, you found me.</h1>" \
        "<img height='400' \
        style='display: block; margin-left: auto; margin-right: auto;' \
        src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    if number > random_number:
        return too_high
    elif number < random_number:
        return too_low
    else:
        return just_right
        

if __name__ == "__main__":
    app.run(debug=True)

