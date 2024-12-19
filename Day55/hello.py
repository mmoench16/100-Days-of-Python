from flask import Flask

app = Flask(__name__)

# Decorator functions ⬇️
def make_bold(func):
    """
    Decorator function that wraps the output of the given function
    in HTML bold tags (<b></b>), which typically bolds the text in HTML.
    """
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    """
    Decorator function that wraps the output of the given function
    in HTML emphasis tags (<em></em>), which typically italicizes
    the text in HTML.
    """

    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper
# Decorator functions ⬆️

def make_underlined(func):
    """
    Decorator function that wraps the output of the given function
    in HTML underline tags (<u></u>), which typically underlines
    the text in HTML.
    """

    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!" \
        "</h1><p>This is a paragraph</p>" \
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGpxY3RieTI4emd2ODQzc2IyZ3hhZTdrcTYzdWNlaHowZTYyOGkxNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif'>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye</p>"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello there {name.capitalize()}</p>"

if __name__ == "__main__":
    app.run(debug=True)

