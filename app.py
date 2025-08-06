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
@app.route("/Ans1",methods=["POST"])
def Ans1():
    form_data = request.form.get("options")
    return render_template("Anspg1.html",data=form_data)

@app.route("/Ans2",methods=["POST"])
def Ans2():
     form_data = request.form.get("options")
     return render_template("Anspg2.html",data=form_data)

@app.route("/Ans3",methods=["POST"])
def Ans3():
     form_data = request.form.get("options")
     return render_template("Anspg3.html",data=form_data)

@app.route("/Ans4",methods=["POST"])
def Ans4():
     form_data = request.form.get("options")
     return render_template("Anspg4.html",data=form_data)

@app.route("/Ans5",methods=["POST"])
def Ans5():
     form_data = request.form.get("options")
     return render_template("Anspg5.html",data=form_data)

@app.route("/Ans6",methods=["POST"])
def Ans6():
     form_data = request.form.get("options")
     return render_template("Anspg6.html",data=form_data)

    
# main driver function
if __name__ == '__main__':

 app.run(debug=True)

