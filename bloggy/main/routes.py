from flask import (
    Blueprint, render_template, request, session)
from bloggy import app, mongo, ObjectId
from flask_paginate import Pagination, get_page_parameter
from bloggy.utilities import (all_posts, get_user_id_from_username)

main = Blueprint("main", __name__)


@main.route('/', methods=("GET", "POST"))
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
    get_all_posts_pagination = mongo.db.posts.find().skip(
        (page-1) * per_page).limit(per_page)
    # Handle sorting if value is X sort by Y
    if request.form.get('sort') == "1":
        all_posts = get_all_posts_pagination.sort("last_updated", -1)
    if request.form.get('sort') == "2":
        all_posts = get_all_posts_pagination.sort("last_updated", 1)
    if request.form.get('sort') == "3":
        all_posts = get_all_posts_pagination.sort("title", 1)
    if request.form.get('sort') == "4":
        all_posts = get_all_posts_pagination.sort("title", -1)
    if request.form.get('sort') == "5":
        all_posts = get_all_posts_pagination.sort("views", -1)
    if request.form.get('sort') is None:
        all_posts = get_all_posts_pagination
    sorting_value = request.form.get('sort')
    # Define pagination
    pagination = Pagination(
        page=page, per_page=per_page,
        total=all_posts.count(), record_name='posts')
    # Get current user's id
    current_user = session.get("user")
    if current_user is None:
        return render_template(
            'index.html', all_posts=all_posts,
            pagination=pagination, sorting_value=sorting_value)
    current_user_id = get_user_id_from_username(current_user)
    return render_template(
        'index.html', all_posts=all_posts,
        pagination=pagination, sorting_value=sorting_value,
        current_user_id=current_user_id, current_user=current_user)


@main.route('/search', methods=("GET", "POST"))
def search():
    search_request = request.form.get("search")
    all_posts = mongo.db.posts.find({"$text": {"$search": search_request}})
    return render_template(
        'search.html', all_posts=all_posts, search_request=search_request)
