from flask import Flask, render_template, request
import requests, smtplib, os
from dotenv import load_dotenv

posts = requests.get("https://api.npoint.io/8be439e2d02333d46d42").json()

app = Flask(__name__)

load_dotenv()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=[ "GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        # print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("APP_PASSWORD")
        recipeint_email = os.getenv("RECIPIENT_EMAIL")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=recipeint_email, 
                                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message
                                }")

        return render_template("contact.html", msg_sent=True) 
    return render_template("contact.html", msg_sent=False)   

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
