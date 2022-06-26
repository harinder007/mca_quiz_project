from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/about")
def aboutPage():
    return render_template('about.html')

@app.route("/javaQuiz")
def javaQuiz():
    return render_template('javaQuiz.html')

@app.route("/cQuiz")
def cQuiz():
    return render_template('cQuiz.html')