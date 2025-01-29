from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
all_posts = response.json()

@app.route('/')
def home():
    
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def post(post_id):

    post = next((post for post in all_posts if post['id'] == post_id), None)

    return render_template("post.html", post=post, id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
