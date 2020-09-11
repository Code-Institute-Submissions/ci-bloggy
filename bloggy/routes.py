from flask import (
    render_template, redirect,
    request, session, url_for, flash)
from bloggy import app, mongo, bcrypt
from bloggy.forms import RegisterForm, LoginForm
from bloggy.utilities import all_posts, featured_posts
from slugify import slugify

'''Define index route'''
@app.route('/')
def index():
    return render_template('index.html', all_posts=all_posts, featured_posts=featured_posts)

'''Define login route'''
@app.route('/login', methods=("GET", "POST"))
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

'''Define register route'''
@app.route('/register', methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            register_user = {
                "username": form.username.data,
                "password": hashed_password,
                "email": form.email.data,
            }
            registered_usr_id = mongo.db.users.insert_one(register_user)
            register_blog = {
                "owner_id": str(registered_usr_id.inserted_id),
                "title": form.blog_title.data,
                "title-slug": slugify(form.blog_title.data),
                "description": form.blog_description.data
            }
            mongo.db.blogs.insert_one(register_blog)
            flash("You have been sucessfully registered, you can now log in below")
            return redirect(url_for('login'))
    return render_template('register.html', form=form)
