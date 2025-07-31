#starter code/Boiler plate
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route("/")
def index():
    
    return render_template("index.html")
#connection setup for game page 
@app.route("/Gamepg")
def gamePg():
    return render_template("Gamepg.html")
# main driver function
if __name__ == '__main__':

 app.run(debug=True)

