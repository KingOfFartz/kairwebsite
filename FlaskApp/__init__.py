from flask import Flask
from FlaskApp import config
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

from FlaskApp import routes

if __name__ == "__main__":
    app.run(DEBUG=True)
