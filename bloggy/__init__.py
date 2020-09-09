import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# * Import env from env.py file
if os.path.exists("./env.py"):
    import env

app = Flask(__name__)
app.config["MONO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["RECAPTCHA_PUBLIC_KEY"]=os.environ.get("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_SECRET_KEY"]=os.environ.get("RECAPTCHA_SECRET_KEY")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

from bloggy import routes

