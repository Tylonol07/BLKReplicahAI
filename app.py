#starter code/Boiler plate
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
#Quiz routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Quiz1")
def quiz1():
    return render_template("Quizpg1.html")

@app.route("/Quiz2")
    # data = request.form[""]
def quiz2():
    return render_template("Quizpg2.html")

@app.route("/Quiz3")
def quiz3():
    return render_template("Quizpg3.html")

@app.route("/Quiz4")
def quiz4():
    return render_template("Quizpg4.html")

@app.route("/Quiz5")
def quiz5():
    return render_template("Quizpg5.html")

@app.route("/Quiz6")
def quiz6():
    return render_template("Quizpg6.html")
#Answer routes
@app.route("/Ans1")
def Ans1():
    return render_template("Anspg1.html")

@app.route("/Ans2")
def Ans2():
    return render_template("Anspg2.html")

@app.route("/Ans3")
def Ans3():
    return render_template("Anspg3.html")

@app.route("/Ans4")
def Ans4():
    return render_template("Anspg4.html")

@app.route("/Ans5")
def Ans5():
    return render_template("Anspg5.html")

@app.route("/Ans6")
def Ans6():
    return render_template("Anspg6.html")

#connection setup for game page 
@app.route("/Gamepg")
def gamePg():
    return render_template("Gamepg.html")
# main driver function
if __name__ == '__main__':

 app.run(debug=True)

