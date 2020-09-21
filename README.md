# Bloggy - The home of blogs you love

![Bloggy logo](bloggy/static/img/logo.svg "Bloggy logo Logo")


Bloggy - write posts, share ideas, discover the world.

Bloggy is a blogging platform where users can create their own blog and post to it about any topic.

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

 
## UX
 
### User stories

📌 As a user I want to access the website, browse and read a post

📌 As a user I want to sort all posts on the website alphabetically, by date, or popularity

📌 As a user I want to search for a particular post

📌 As a user I want to be able to see the author of the post I am reading and other posts that visit their blog

📌 As a user I want to register and create my own blog

📌 As a user I want to post posts to my blog

📌 As a user I want to be able to edit and delete my own posts

### Strategy

The main design goal is to provide users with clean and sleek website with easy-to-read textual content that is meaningfully organised.

### Scope

For readers Bloggy is a way to read about their favourite topics and for creators, Bloggy is a way to put their content out there for the world to see.

### Structure



### Skeleton

Balsamiq Wireframes has been used to develop wireframes for this website.

Wireframes are available under links below and are stored within _wireframes_ folder inside _docs_ folder.


### Surface

![Project colour scheme](./bloggy/docs/colour-scheme.png "Project colour scheme")

| Colour name       | Colour RGB Code    
| -------------     |:-------------:| 
| Bleu De France    |#1585E2
| Flickr Pink       |#F1007C
| White             |#FFFFF

Font used on the website is Noto Sans KR from Google Fonts - https://fonts.google.com/specimen/Noto+Sans+KR?query=noto+sans+kr

## Features


### Existing Features

🟢 **Home page**

Home page displays all posts to the user and user is able to search for specific post based on title, description or body of the post and is able to sort all posts by: Newest first, oldest first, title (A-Z), title (Z-A) & popularity (based on number of views).
User can also click on 'Start creating' to either log in (if not already logged in) or to be redirected to 'New post' page.

🟢 **Login/Register page**

Anyone can register an user account and a blog for free.

When registering user is prompted for their personal details - username, email address and password as well as details about their blog such as blog title and description.

User can also log into their account which if successful will bring them to the user page.

🟢 **User page**

User page (profile page) is where user view all their posts (in a card view), read the post, edit the post or delete the post.

🟢 **New post page**

Registered users can create new posts by clicking 'Start creating' on home page or by clicking 'New Post' on their user page.

To create new post, users need to:
1. Give the post a title, 
2. Add some text to the body of the blog, 
3. Add short description (blurb), 
4. Provide a URL to an image to be used as a cover
5. Provide at least 2 tags to the post 
6. Add in approximate reading time

🟢 **Edit post page**

Only post creator (& superuser Admin) can edit a post.

The form is exactly the same as outlined in [new post page](#new-post-page) section above but it is pre-filled with post data pulled from the database.

### Features Left to Implement

🔴 **Feature left to implement**

## Technologies Used

1. HTML5
2. CSS3
5. JavaScript
3. Python 
4. [Flask v1.1.2](https://flask.palletsprojects.com/en/1.1.x/changelog/#version-1-1-x)
  * WTForms 
  * PyMongo
  * Slugify
  * Bcrypt
5. [Summernote WYSIWYG Editor](https://summernote.org/)
5. MongoDB 
3. [Materialize CSS](https://materializecss.com/)
4. [Materialize Icons](https://materializecss.com/icons.html)
7. [Google Fonts](https://fonts.google.com/)

## Testing


## Deployment

### To deploy locally

Pre-requirements to deploy this project are:
1. You must have [Python3](https://www.python.org/downloads/) installed as well as [PIP](https://pip.pypa.io/en/stable/installing/) to install all dependencies
2. A code editor of your choice such as [VSCode](https://code.visualstudio.com/) or [Atom](https://atom.io/). 
3. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to pull data from github
4. [MongoDB](https://www.mongodb.com/) to store data into the database (note you'll need to create one on your own using details provided below)

Once all this is in place follow the steps below:
1. Clone this git repo using GIT CLI:
    *  `git clone https://github.com/ib-skoric/ci-bloggy.git`
2. Create `env.py` file that contains correct MONGO_URI and login credentials as well as all SECRET KEY values required for CAPTCHA & other modules
3. Run `FLASK_APP=run.py` & `FLASK_ENV=development` or alternatively create a `flaskenv` file with these commands
4. Install all required modules from the `requirements.txt` file:
    * `sudo -H pip3 -r requirements.txt`
5. Sign up for a free MongoDB account via this [link](https://www.mongodb.com/) and create a new collection called __bloggy__ (note all lowercase letters)

### Collections structure 

**blogs structure**

| Field name       | Data type   
| -------------     |:-------------:| 
| _id               | ObjectId()
| owner_id          | ObjectId()
| title             | String
| description       | String

**posts structure**

| Field name       | Data type   
| -------------     |:-------------:| 
| _id               | ObjectId()
| blog_id           | ObjectId()
| user_id           | ObjectId()
| title             | String
| description       | String
| body       | String
| last_updated       | String
| tags       | String
| read_time       | Int32
| is_featured       | Boolean
| img_url       | String
| views       | Int32


**user structure**
| Field name       | Data type   
| -------------     |:-------------:| 
| _id               | ObjectId()
| username          | String
| email             | String
| password          | String


## Credits


### Content

__All posts posted on Bloggy are under sole copyright of their respective creators and the creator of this application (Ivan Branimir Skoric) is not responsible for any copyright breaches or foul language that could be contained within users' posts__

### Media

__All images posted on Bloggy are under sole copyright of their respective creators and the creator application (Ivan Branimir Skoric) is not responsible for any copyright breaches that could be commited by other users__

SVG Illustration used in jumbotron have been sourced from [Undraw](https://undraw.co/illustrations). 

### Acknowledgements

[Tim Nelson](https://github.com/TravelTimN) for his great updated Flask tutorials that he sent me after I posted a question about MongoDB and Flask.
