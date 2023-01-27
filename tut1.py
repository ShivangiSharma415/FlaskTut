from flask import Flask, render_template  #Flask module se flask class import kiye h or uss class ka ek instance bana rahe hai

app = Flask(__name__)  #instance of that class 

@app.route("/")   #ek route define kar dia mtlb endpoint
def hello_world():
    return render_template("index.html")

@app.route("/about")   #ek route define kar dia mtlb endpoint
def hello():
    name = "Shivangi"
    return render_template("about.html", myname = name)

app.run(debug=True)