from flask import (
    Blueprint, render_template, redirect,
    request, session, url_for, flash)
from bloggy import app, mongo, bcrypt, ObjectId
from bloggy.forms import RegisterForm, LoginForm
from slugify import slugify
from flask_paginate import Pagination, get_page_parameter
from bloggy.utilities import (check_username,
                              get_user_id_from_username, get_users_posts)

user = Blueprint("user", __name__)

@user.route('/login', methods=("GET", "POST"))
def login():
    '''Define login route'''
    # Check if user is in session, if true redirect them to user page
    if "user" in session:
        return redirect(url_for('user.user_page'))
    # Define WTForms form
    form = LoginForm()
    # Check form validation refer to forms.py file for validators
    if form.validate_on_submit():
        # Check username in database
        user = check_username(form.username.data)
        # Get users password
        user_password = user["password"]
        # Get input field password
        input_password = form.password.data
        # Check if credentials match
        if bcrypt.check_password_hash(user_password, input_password):
            session["user"] = form.username.data.lower()
            flash("You've been logged in successfully")
            return redirect(url_for('user.user_page'))
        # Else if they don't:
        else:
            flash("Details incorrect")
    return render_template('login.html', form=form)


@user.route('/logout')
def logout():
    '''Define log out route'''
    # Pop the user out of the session
    session.pop("user")
    flash("You have been logged out successfully")
    return redirect(url_for('main.index'))


@user.route('/register', methods=("GET", "POST"))
def register():
    '''Define register route'''
    # Define WTForms form
    form = RegisterForm()
    if form.validate_on_submit():
            # Hash the password from the input field first
            hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            # Define register_user dictionary
            register_user = {
                "username": form.username.data,
                "password": hashed_password,
                "email": form.email.data,
                "profile_img_url": form.profile_img_url.data
            }
            # Get the inserted user's ID
            registered_usr_id = mongo.db.users.insert_one(register_user)
            # Define register blog dictionary
            register_blog = {
                "owner_id": ObjectId(registered_usr_id.inserted_id),
                "title": form.blog_title.data,
                "title-slug": slugify(form.blog_title.data),
                "description": form.blog_description.data
            }
            # Insert blog details into the database
            mongo.db.blogs.insert_one(register_blog)
            # All goes well display flash message & return user to login form
            flash(
                "You have been sucessfully registered, you can now log in below")
            return redirect(url_for('user.login'))
    return render_template('register.html', form=form)


@user.route('/user')
def user_page():    
    '''Define user page route'''
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 6
    # Get current user
    current_user = session.get("user")
    # Check if user is admin if it is, display all posts
    if current_user == 'admin':
        users_posts = mongo.db.posts.find().skip((page-1) * per_page).limit(per_page)
    if current_user != 'admin':
    # Get current user ID
        current_user_id = ObjectId(get_user_id_from_username(current_user))
        # Get current user's posts
        users_posts = get_users_posts(current_user_id).skip((page-1) * per_page).limit(per_page)
    pagination = Pagination(
        page=page, per_page=per_page, total=users_posts.count(),
        record_name='users_posts')
    return render_template('user.html', users_posts=users_posts, pagination=pagination)





