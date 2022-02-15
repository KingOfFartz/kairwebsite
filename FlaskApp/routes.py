from flask import render_template, request
from FlaskApp import app
import os

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/update", methods=['GET'])
def update():
    
    app.config.from_object
    test = request.args.get('test')
    if os.path.isfile("/var/www/FlaskApp/FlaskApp/writetest/myfile.txt"):
        f = open("/var/www/FlaskApp/FlaskApp/writetest/myfile.txt", "a")
        string1 = test + "\n"
        f.write(string1)
        f.close()
    else:
        f = open("/var/www/FlaskApp/FlaskApp/writetest/myfile.txt", "x")
        f.write(test)
        f.close()
    return render_template("update.html", value=test)


