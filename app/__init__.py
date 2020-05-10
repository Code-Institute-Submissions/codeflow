import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config.from_object(Config)

mongo = PyMongo(app)


from app import routes

