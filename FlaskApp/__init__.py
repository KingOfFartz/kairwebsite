from flask import Flask
from FlaskApp import config
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
"""
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_tempalte("about.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")
"""
from FlaskApp import routes
