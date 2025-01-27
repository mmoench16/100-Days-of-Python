from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    name = name.lower()
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()

    age = data["age"]

    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()

    gender = data["gender"]

    return render_template('guess.html', name=name.capitalize(), age=age, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)