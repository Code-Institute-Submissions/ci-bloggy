import os
from flask import (
    Flask, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin
# * Import env from env.py file
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
'''Required code to initiate flask_login'''
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return mongo.db.users.find_one({user_id})

'''Define index route'''
@app.route('/')
def index():
    all_posts = mongo.db.posts.find()
    featured_posts = mongo.db.posts.find({"is_featured": True})
    return render_template('index.html', all_posts=all_posts, featured_posts=featured_posts)

'''Define login route'''
@app.route('/login')
def login():
    
    return render_template('login.html')

'''Define register route'''
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
  app.run(
      host=os.environ.get("IP"),
      port=int(os.environ.get("PORT")), 
      debug=True)