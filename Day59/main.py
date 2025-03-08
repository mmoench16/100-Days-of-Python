from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/8be439e2d02333d46d42")
response.raise_for_status()
all_posts = response.json()

@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = next((post for post in all_posts if post["id"] == post_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)