#!/usr/bin/python
activate_this = '/var/www/FlaskApp/flaskenv/bin/activate_this.py'
with open(activate_this_ as file_:
     exec(file_.read(). dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='/var/www/html/FlaskApp/kair/logs/kair.log', format='%(asctime)s %(message)s')
sys.path.insert(0, '/var/www/html/FlaskApp/kair/')
sys.path.insert(0, '/var/www/html/FlaskApp/flaskenv/lib/python3.8/site-packages')
from kair import app as application