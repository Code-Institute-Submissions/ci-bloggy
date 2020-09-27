import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
# * Import env from env.py file
if os.path.exists("./env.py"):
    import env

app = Flask(__name__)
app.config["MONO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["RECAPTCHA_PUBLIC_KEY"] = os.environ.get("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.environ.get("RECAPTCHA_PRIVATE_KEY")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


# Import routes and register blueprints
from main.routes import main
from profile.routes import profile
from user.routes import user
from post.routes import post
app.register_blueprint(main)
app.register_blueprint(profile)
app.register_blueprint(user)
app.register_blueprint(post)
