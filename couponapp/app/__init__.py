#Init file

from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.mongokit import MongoKit, Document, Connection
from flask.ext.login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object('config')

#Mongo Connection
app.config["MONGO_DATABASE"] = 'couponext'
app.config["MONGO_HOST"] = '127.0.0.1'
app.config["MONGO_PORT"] = 27017

mongo = MongoKit(app)

from app import views
