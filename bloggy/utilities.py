from bloggy import mongo

# -------------------------------------- #
#    Database filtering/query helpers    #
# -------------------------------------- #
all_posts = list(mongo.db.posts.find()) # Fetch all posts from the database
featured_posts = list(mongo.db.posts.find({"is_featured": True})) # Fetch featured posts from database

def check_username(username):
    return mongo.db.users.find_one({"username": username.lower()})

def check_email(email):
    return mongo.db.users.find_one({"email": email})

def check_existing_blog(blog_name):
    return mongo.db.blogs.find_one({"title-slug": blog_name})

def get_current_user_id(username):
    return mongo.db.users.find_one({"username": username})["_id"]

def get_users_posts(user_id):
    return list(mongo.db.posts.find({"user_id": user_id}))
