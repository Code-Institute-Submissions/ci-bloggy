from flask import (
    Blueprint, render_template, redirect,
    request, session, url_for, flash)
from bloggy import app, mongo, ObjectId
from bloggy.forms import PostForm
from datetime import datetime
from bloggy.utilities import (all_posts, check_username,
                              get_user_id_from_username, get_user_from_id, get_blog_from_user_id)


post = Blueprint("post", __name__)


@post.route('/user/new_post', methods=("GET", "POST"))
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
        user_id = ObjectId(get_user_id_from_username(current_user))
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
                    "username": current_user,
                    "title": form.title.data,
                    "description": form.description.data,
                    "body": post_body,
                    "last_updated": datetimesting,
                    "read_time": form.read_time.data,
                    "image_url": form.image_url.data,
                    "views": 0
                }
                mongo.db.posts.insert_one(new_post)
                # All goes well flash the message and
                # return them to the home page
                flash("Your post has been submitted successfully.")
                return redirect(url_for('user.user_page'))
    # Else if user is not logged in flash message and promt them to log in
    else:
        flash('You must be logged in to create a new post')
        return redirect(url_for('user.login'))
    return render_template('new_post.html', form=form)


@post.route('/posts/<post_id>')
def post_page(post_id):
    '''Define single post page route'''
    # Get the post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    # Get the creator
    creator = get_user_from_id(post["user_id"])
    current_views = post["views"]
    # Increment views by 1
    mongo.db.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"views": 1}})
    return render_template('post.html', post=post, creator=creator)


@post.route('/posts/<post_id>/edit/', methods=("GET", "POST"))
def edit_post(post_id):
    '''Define edit post route'''
    # Define WTForms form
    form = PostForm()
    # Get post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    post_body = request.form.get('post_body')
    # Get current user ID
    current_user = session.get("user")
    # Check if logged in, if not flash message and redirect to home page
    if current_user is None:
        flash("You don't have permission to edit this post")
        return redirect(url_for('main.index'))
    # Check if user is admin if it is, inject correct user id based
    # on the post to allow editing
    if current_user == 'admin':
        current_user_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    if current_user != 'admin':
        '''Check what are current user ID and post creator IDs
        (ie.AssertionError if the user is post owner)'''
        current_user_id = ObjectId(get_user_id_from_username(current_user))
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    '''Check if user is allowed to edit the post
    if not flash message and redirect to user page'''
    if current_user_id != post_creator_id:
        flash("You don't have permission to edit this post")
        return redirect(url_for('user.user_page'))
    '''If anonymous tries to access edit post page
    flash them message and redirect to home page'''
    if current_user is None:
        flash("You don't have permission to edit this post")
        return redirect(url_for('main.index'))
    if form.is_submitted() and form.validate() == False:
        '''Form a fake post dict to pass onto the template and preserve already edited data'''
        post_id = mongo.db.posts.find_one({'_id': ObjectId(post_id)})["_id"]
        post = {
            "_id": post_id,
            "title" : form.title.data,
            "description" : form.description.data,
            "body" : post_body,
            "read_time" : form.read_time.data,
            "image_url" : form.image_url.data
        }
        return render_template('edit_post.html', post=post, form=form, post_id=post_id)
    if form.validate_on_submit():
        # Get data - refer to new post function above
        datetimesting = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        current_views = post["views"]
        current_user = session.get("user")
        user_id = ObjectId(get_user_id_from_username(current_user))
        blog_id = ObjectId(
            mongo.db.blogs.find_one(
                {"owner_id": user_id})["_id"])
        update_post = {
                    "blog_id": blog_id,
                    "user_id": user_id,
                    "username": current_user,
                    "title": form.title.data,
                    "description": form.description.data,
                    "body": post_body,
                    "last_updated": datetimesting,
                    "read_time": form.read_time.data,
                    "image_url": form.image_url.data,
                    "views": current_views
                }
        mongo.db.posts.update(post, update_post)
        flash("Post updated successfully")
        return redirect(url_for('user.user_page'))
    return render_template('edit_post.html', post=post, form=form)


@post.route('/posts/<post_id>/delete', methods=("GET", "POST"))
def delete_post(post_id):
    '''Define delete post route'''
    # Get post ID
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    # Get current user
    current_user = session.get("user")
    # Check if user is logged in, if not flash message & redirect to index
    if current_user is None:
        flash("You don't have permission to delete this post")
        return redirect(url_for('main.index'))
    # Check if user is admin if it is, inject 
    # correct user id based
    # on the post to allow deletion
    if current_user == 'admin':
        current_user_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    if current_user != 'admin':
        current_user_id = ObjectId(get_user_id_from_username(current_user))
        post_creator_id = mongo.db.posts.find_one(
            {'_id': ObjectId(post_id)})["user_id"]
    # Check if user id and post creator Id match
    if current_user_id != post_creator_id:
        flash("You don't have permission to delete this post")
        return redirect(url_for('main.index'))
    '''Else user is authorised to delete so
    proceed & redirect user back to home page'''
    mongo.db.posts.delete_one(post)
    flash("Post deleted successfully")
    return redirect(url_for('user.user_page'))