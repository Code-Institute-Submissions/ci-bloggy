from bloggy import mongo

# -------------------------------------- #
#    Database filtering/query helpers    #
# -------------------------------------- #
all_posts = mongo.db.posts.find() # Fetch all posts from the database
featured_posts = mongo.db.posts.find({"is_featured": True}) # Fetch featured posts from database

def existing_user(existing_username):
    return mongo.db.users.find_one({"username": existing_username.lower()})

def existing_email(existing_email):
    return mongo.db.users.find_one({"email": existing_email})

def existing_blog(existing_blog_name):
    return mongo.db.blogs.find_one({"title-slug": existing_blog_name})
