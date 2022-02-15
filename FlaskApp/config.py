import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE = os.environ.get('DATABASE_FILE')
    DEBUG = True
    TESTING = True
