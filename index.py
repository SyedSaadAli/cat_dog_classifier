from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/welcome/<welcome>")
def hello(welcome):
    return f"Hello, {escape(welcome)}!"

@app.route("/test")
def test():
    return "Test route is working"

@app.route("/test2")
def test2():
    return "Test2 route is working"

@app.route("/test3")
def test3():
    return "Test3 route is working"