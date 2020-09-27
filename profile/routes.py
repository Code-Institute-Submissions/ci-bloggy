from flask import (
    Blueprint, render_template, request)
from bloggy import app, mongo
from flask_paginate import Pagination, get_page_parameter
from bloggy.utilities import (get_users_posts, get_blog_from_user_id, get_user_from_username)

profile = Blueprint("profile", __name__)


@profile.route('/profile/<username>')
def profile_page(username):
    '''Define user profile page route'''
    # Define per page posts number
    per_page = 6
    # Define page arg
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # Get user from the database
    profile = get_user_from_username(username)
    # Get user ID from database
    profile_id = profile["_id"]
    # Get user's blog
    profile_blog = get_blog_from_user_id(profile_id)
    # Get users posts from database
    profile_posts = get_users_posts(profile_id).skip((page-1) * per_page).limit(per_page)
    # Define pagination
    pagination = Pagination(
        page=page, per_page=per_page, total=profile_posts.count(),
        record_name='posts')
    return render_template('profile.html', profile=profile, profile_posts=profile_posts, profile_blog=profile_blog, pagination=pagination)