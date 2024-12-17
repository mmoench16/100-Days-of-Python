from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!" \
        "</h1><p>This is a paragraph</p>" \
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGpxY3RieTI4emd2ODQzc2IyZ3hhZTdrcTYzdWNlaHowZTYyOGkxNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif'>"

@app.route("/bye")
def say_bye():
    return "<p>Bye</p>"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello there {name.capitalize()}</p>"

if __name__ == "__main__":
    app.run(debug=True)