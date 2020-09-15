from flask import (
    render_template, redirect,
    request, session, url_for, flash)
from bloggy import app, mongo, bcrypt, ObjectId
from bloggy.forms import RegisterForm, LoginForm, NewPostForm
from bloggy.utilities import all_posts, featured_posts, check_username, get_current_user_id, get_users_posts
from slugify import slugify
from datetime import datetime

'''Define index route'''
@app.route('/')
def index():
    return render_template('index.html', all_posts=all_posts, featured_posts=featured_posts)

'''Define login route'''
@app.route('/login', methods=("GET", "POST"))
def login():
    if "user" in session:
        return redirect(url_for('user_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = check_username(form.username.data)
        user_password = user["password"]
        input_password = form.password.data
        if bcrypt.check_password_hash(user_password, input_password):
            session["user"] = form.username.data.lower()
            flash ("You've been logged in successfully")
            return redirect(url_for('user_page'))
        else:
            flash ("Details incorrect")
    return render_template('login.html', form=form)

'''Define log out route'''
@app.route('/logout')
def logout():
    session.pop("user")
    flash("You have been logged out successfully")
    return redirect(url_for('index'))

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
                "owner_id": ObjectId(registered_usr_id.inserted_id),
                "title": form.blog_title.data,
                "title-slug": slugify(form.blog_title.data),
                "description": form.blog_description.data
            }
            mongo.db.blogs.insert_one(register_blog)
            flash("You have been sucessfully registered, you can now log in below")
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/user')
def user_page():
    current_user = session.get("user")
    current_user_id = ObjectId(get_current_user_id(current_user))
    users_posts = get_users_posts(current_user_id)
    return render_template('user.html', users_posts=users_posts)

@app.route('/user/new_post', methods=("GET", "POST"))
def new_post():
    form = NewPostForm()
    if session.get("user") != None:
        current_user = session.get("user")
        post_body = request.form.get('post_body')
        datetimesting = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        user_id = ObjectId(get_current_user_id(current_user))
        blog_id = ObjectId(mongo.db.blogs.find_one({"owner_id": user_id})["_id"])
        if form.validate_on_submit():
            if post_body != '':
                new_post = {
                    "blog_id": blog_id,
                    "user_id": user_id,
                    "title": form.title.data,
                    "body": post_body,
                    "last_updated": datetimesting,
                    "category": "Test",
                    "read_time": "10 minutes",
                    "is_featured": False,
                    "image_url": form.image_url.data
                }
                mongo.db.posts.insert_one(new_post)
                flash ("Your post has been submitted successfully.")
                return redirect(url_for('user_page'))
    flash('You must be logged in to create a new post')
    return redirect(url_for('login'))

'''Define single post page route'''
@app.route('/posts/<post_id>')
def post_page(post_id):
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    return render_template('post.html', post=post)