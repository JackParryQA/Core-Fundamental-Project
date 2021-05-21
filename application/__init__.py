from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
# app.config['SECRET_KEY'] = 'sfiunsioudhao98'

db = SQLAlchemy(app)

from application import routes