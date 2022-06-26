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

@app.route("/pythonQuiz")
def pythonQuiz():
    return render_template('pythonQuiz.html')

@app.route("/csshtmlQuiz")
def cssHtmlQuiz():
    return render_template('htmlCssQuiz.html')

@app.route("/sqlQuiz")
def sqlQuiz():
    return render_template('sqlQuiz.html')

@app.route("/javascriptQuiz")
def javascriptQuiz():
    return render_template('jsQuiz.html')