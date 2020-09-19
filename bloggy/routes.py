from flask import (
    render_template, redirect,
    request, session, url_for, flash)
from bloggy import app, mongo, bcrypt, ObjectId
from bloggy.forms import RegisterForm, LoginForm, PostForm
from slugify import slugify
from datetime import datetime
from flask_paginate import Pagination, get_page_parameter
from bloggy.utilities import (all_posts, featured_posts,
                              check_username, get_current_user_id,
                              get_users_posts)


@app.route('/')
def index():
    '''Define index/home page route'''
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # Set the limit of posts per page
    per_page = 6
    '''Get all posts from the database and limit
    the results using per_page variable.
    Solution for this was found here:
    https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo
    '''
    all_posts = mongo.db.posts.find().skip((page-1) * per_page).limit(per_page)
    # Define pagination
    pagination = Pagination(
        page=page, per_page=per_page,
        total=all_posts.count(), record_name='posts')
    return render_template(
        'index.html', all_posts=all_posts,
        pagination=pagination)


@app.route('/login', methods=("GET", "POST"))
def login():
    '''Define login route'''
    # Check if user is in session, if true redirect them to user page
    if "user" in session:
        return redirect(url_for('user_page'))
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
            return redirect(url_for('user_page'))
        # Else if they don't:
        else:
            flash("Details incorrect")
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    '''Define log out route'''
    # Pop the user out of the session
    session.pop("user")
    flash("You have been logged out successfully")
    return redirect(url_for('index'))


@app.route('/register', methods=("GET", "POST"))
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
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/user')
def user_page():
    '''Define user page route'''
    # Get current user
    current_user = session.get("user")
    # Get current user ID
    current_user_id = ObjectId(get_current_user_id(current_user))
    # Get current user's posts
    users_posts = get_users_posts(current_user_id)
    return render_template('user.html', users_posts=users_posts)


@app.route('/user/new_post', methods=("GET", "POST"))
def new_post():
    '''Define new post route'''
    # Define WTForms form
    form = PostForm()
    # Check if user is in session
    if session.get("user") is not None:
        # Get current user
        current_user = session.get("user")
        # Get post body from Summernote WYSIWYG editor
        post_body = request.form.get('post_body')
        # Get current date and time
        datetimesting = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Get current user ID
        user_id = ObjectId(get_current_user_id(current_user))
        # Get current user's blog's ID
        blog_id = ObjectId(
            mongo.db.blogs.find_one(
                {"owner_id": user_id})["_id"])
        if form.validate_on_submit():
            # Check that body is not empty
            if post_body != '':
                # Define new post dictionary
                new_post = {
                    "blog_id": blog_id,
                    "user_id": user_id,
                    "title": form.title.data,
                    "body": post_body,
                    "last_updated": datetimesting,
                    "tags": form.tags.data,
                    "read_time": form.read_time.data + " minutes",
                    "is_featured": False,
                    "image_url": form.image_url.data
                }
                mongo.db.posts.insert_one(new_post)
                # All goes well flash the message and
                # return them to the home page
                flash("Your post has been submitted successfully.")
                return redirect(url_for('user_page'))
    # Else if user is not logged in flash message and promt them to log in
    else:
        flash('You must be logged in to create a new post')
        return redirect(url_for('login'))
    return render_template('new_post.html', form=form)


@app.route('/posts/<post_id>')
def post_page(post_id):
    '''Define single post page route'''
    # Get the post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    return render_template('post.html', post=post)


@app.route('/posts/<post_id>/edit', methods=("GET", "POST"))
def edit_post(post_id):
    '''Define edit post route'''
    # Define WTForms form
    form = PostForm()
    # Get post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    # Get current user ID
    current_user = session.get("user")
    # Check if logged in, if not flash message and redirect to home page
    if current_user is None:
        flash("You don't have permission to edit this post")
        return redirect(url_for('index'))
    else:
        '''Check what are current user ID and post creator IDs
        (ie.AssertionError if the user is post owner)'''
        current_user_id = ObjectId(get_current_user_id(current_user))
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    '''Check if user is allowed to edit the post
    if not flash message and redirect to user page'''
    if current_user_id != post_creator_id:
        flash("You don't have permission to edit this post")
        return redirect(url_for('user_page'))
    '''If anonymous tries to access edit post page
    flash them message and redirect to home page'''
    if current_user is None:
        flash("You don't have permission to edit this post")
        return redirect(url_for('index'))
    if form.validate_on_submit():
        # Get data - refer to new post function above
        datetimesting = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        post_body = request.form.get('post_body')
        current_user = session.get("user")
        user_id = ObjectId(get_current_user_id(current_user))
        blog_id = ObjectId(
            mongo.db.blogs.find_one(
                {"owner_id": user_id})["_id"])
        update_post = {
                    "blog_id": blog_id,
                    "user_id": user_id,
                    "title": form.title.data,
                    "body": post_body,
                    "last_updated": datetimesting,
                    "tags": form.tags.data,
                    "read_time": form.read_time.data + " minutes",
                    "is_featured": False,
                    "image_url": form.image_url.data
                }
        mongo.db.posts.update(post, update_post)
        flash("Post updated successfully")
        return redirect(url_for('user_page'))
    return render_template('edit_post.html', post=post, form=form)


@app.route('/posts/<post_id>/delete', methods=("GET", "POST"))
def delete_post(post_id):
    '''Define delete post route'''
    # Get post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    # Get current user
    current_user = session.get("user")
    # Check if user is logged in, if not flash message & redirect to index
    if current_user is None:
        flash("You don't have permission to delete this post")
        return redirect(url_for('index'))
    else:
        current_user_id = ObjectId(get_current_user_id(current_user))
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    # Check if user id and post creator Id match
    if current_user_id != post_creator_id:
        flash("You don't have permission to delete this post")
        return redirect(url_for('user_page'))
    '''Else user is authorised to delete so
    proceed & redirect user back to home page'''
    mongo.db.posts.delete_one(post)
    flash("Post deleted successfully")
    return redirect(url_for('user_page'))
    return render_template('user_page')
