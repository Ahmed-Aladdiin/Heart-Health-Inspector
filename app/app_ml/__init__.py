from flask import Flask
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'my_secret')

from app_ml import routes