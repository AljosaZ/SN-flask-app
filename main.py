import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/survey")
def survey():
    return render_template("survey.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/portfolio/hairsalon")
def hairsalon():
    return render_template("hairsalon.html")


if __name__ == "__main__":
    app.run()