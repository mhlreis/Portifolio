from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/portifolio.html")
def portifolio():
    return render_template("portifolio.html")

@app.route("/hobbies.html")
def hobbies():
    return render_template("hobbies.html")

@app.route("/curriculo.html")
def curriculo():
    return render_template("curriculo.html")