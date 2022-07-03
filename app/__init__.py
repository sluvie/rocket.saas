from flask import Flask ## import Flask dari package flask

app = Flask(__name__)

# Setup the app with config.py file
app.config.from_object('app.config')

# Setup the logger
from app.logger_setup import logger

# Set secret key
app.secret_key = app.config['SECRET_KEY']

from app.controllers import  *