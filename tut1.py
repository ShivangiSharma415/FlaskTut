from flask import Flask #Flask module se flask class import kiye h or uss class ka ek instance bana rahe hai

app = Flask(__name__) #instance of that class 

@app.route("/")  #ek route define kar dia mtlb endpoint
def hello_world():
    return "Hello, World!"

@app.route("/hello")  #ek route define kar dia mtlb endpoint
def hello():
    return "Hello, Shivangi"

app.run(debug=True)