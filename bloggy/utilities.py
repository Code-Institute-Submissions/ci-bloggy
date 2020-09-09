from bloggy import mongo

all_posts = mongo.db.posts.find()
featured_posts = mongo.db.posts.find({"is_featured": True})