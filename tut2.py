from flask import Flask, render_template  

app = Flask(__name__)  

@app.route("/")   
def hello_world():
    return render_template("index.html")

@app.route("/about")   
def hello():
    name = "Shivangi"
    return render_template("about.html", myname = name)

app.run(debug=True)