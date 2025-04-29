from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()
api_token = os.getenv("TMDB_ACCESS_TOKEN")
api_key = os.getenv("TMDB_API_KEY")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class ReviewForm(FlaskForm):
    rating = StringField('Your rating out of 10, e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])    
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

def get_movie_data(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()["results"]
    return data

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)

db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"

with app.app_context():
    db.create_all()

# with app.app_context():
#     existing_movie = db.session.execute(db.select(Movie).filter_by(title="Avatar The Way of Water")).scalar()
#     if not existing_movie:
#         second_movie = Movie(
#             title="Avatar The Way of Water",
#             year=2022,
#             description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#             rating=7.3,
#             ranking=9,
#             review="I liked the water.",
#             img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#         )
#         db.session.add(second_movie)
#         db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = ReviewForm()
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_update.review = form.review.data
        movie_to_update.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        movie_data = get_movie_data(movie_title)
        return render_template("select.html", movie_data=movie_data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    movie_details = get_movie_details(movie_id)
    new_movie = Movie(
        title=movie_details["original_title"],
        year=movie_details["release_date"].split("-")[0],
        description=movie_details["overview"],
        rating=0,
        ranking=movie_details["vote_average"],
        review="Write one :)",
        img_url=f"https://image.tmdb.org/t/p/w500{movie_details['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    print(movie_details)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
