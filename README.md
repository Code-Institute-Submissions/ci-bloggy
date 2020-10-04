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

📌 As a user I want to be able to change my blog description and password

📌 As a user I want to post posts to my blog

📌 As a user I want to be able to edit and delete my own posts

### Strategy

The main design goal is to provide users with clean and sleek website with easy-to-read textual content that is meaningfully organised.

### Scope

For readers Bloggy is a way to read about their favourite topics and for creators, Bloggy is a way to put their content out there for the world to see.

### Structure

Index page features a jumbotron with a slogan of "Home of the blogs you love" and a action button. This action button will either bring the user to the login/register page if they're not logged in or it will read 'Write a new post' if the user is authenticated and will bring them to a page where user is able to write a new post. Underneath the jumbotron, users are able to search for posts by title, description or text within, and are able to sort all the posts visible on the home page by: Newest first, oldest first, title (A-Z), title (Z-A) & popularity (based on number of views).

Search page contains a search bar with search and cancel buttons underneath which found posts are displayed.

Single post page contains the post title & post author details at the top with creator's profile picture and a link to visit their profile/blog. Underneath that is the post image supplied by the user and finally the body of the post.

Profile page/Blog page displays user's blog title & description as well as user's profile picture. Underneath that, all of user's posts are displayed. 

Edit profile page features a form where user is asked for their current password, new password and confirmation of the new password (if they wish to change their password), and a field where they can edit their profile image.

Login page contains simple login form that prompts user for their username and password. Users that aren't registered yet are invited to register underneath the form.

Register form contains seven form fields that asks user for:
1. Username
2. Profile picture URL
3. Email address
4. Blog title
5. Blog description
6. Password & 
7. Repeat of their password

reCAPTCHA is utilised to check that user is not a robot.

Create a post page is a form page that that asks user to input:
* Desired post title
* Post description 
* Body of their post
* Post image URL 
* Read time (in minutes)

### Skeleton

Balsamiq Wireframes has been used to develop wireframes for this website.

Wireframes are available under links below and are stored within _wireframes_ folder inside _docs_ folder.

[Home page wireframe](bloggy/docs/landing-page.png)

[Blog page wireframe](bloggy/docs/blog-page.png)

[Post page wireframe](bloggy/docs/single-post-page.png)

[Login page wireframe](bloggy/docs/login-page.png)

### Surface

![Project colour scheme](./bloggy/docs/colour-scheme.png "Project colour scheme")

| Colour name       | Colour RGB Code    
| -------------     |:-------------:| 
| Bleu De France    |#1585E2
| Flickr Pink       |#F1007C
| White             |#FFFFF

Font used on the website is [Noto Sans KR from Google Fonts](https://fonts.google.com/specimen/Noto+Sans+KR?query=noto+sans+kr)

## Features


### Existing Features

🟢 **Home page** (C**R**UD)

Home page displays all posts to the user and user is able to search for specific post based on title, description or body of the post and is able to sort all posts by: Newest first, oldest first, title (A-Z), title (Z-A) & popularity (based on number of views).
User can also click on 'Start creating' to either log in (if not already logged in) or to be redirected to 'New post' page.

🟢 **Login/Register page** (**CR**UD)

Anyone can register an user account and a blog for free.

When registering user is prompted for their personal details - username, email address and password as well as details about their blog such as blog title and description.

User can also log into their account which if successful will bring them to the user page.

🟢 **User page** (**CR**UD)

User's page is where logged in user's are able view all their posts (in a card view), read the post, edit the post or delete the post.

🟢 **Profile/Blog page** (C**R**UD)

Profile page/Blog page is where anyone can view one user's blog, it's description and all their posts. 

🟢 **New post page** (**C**RUD)

Registered users can create new posts by clicking 'Start creating' on home page or by clicking 'New Post' on their user page.

To create new post, users need to:
1. Give the post a title, 
2. Add some text to the body of the blog, 
3. Add short description (blurb), 
5. Add in approximate reading time

Post image URL is optional and a default image will be assigned should the user decide not to fill out this field.

🟢 **Edit post page** (CR**U**D)

Only post creator (& superuser Admin) can edit a post.

The form is exactly the same as outlined in [new post page](#new-post-page) section above but it is pre-filled with post data pulled from the database.

🟢 **Delete post page** (CRU**D**)

Only post creator (& superuser Admin) can delete a post.

🟢 **Search** (C**R**UD)

Users are able to search for posts based on post title, description or text within the body. 

🟢 **Administrative features** (**CRUD**)

'admin' user is registered by myself and is able to edit and delete all posts for the database. 

### Features Left to Implement

🔴 **Likes/favourites feature**

It would be good to implement a feature that allows users to favourite/like posts and save them to their 'favourites' library.

## Technologies Used

1. HTML5
2. CSS3
3. JavaScript
4. Python 
5. [Flask v1.1.2](https://flask.palletsprojects.com/en/1.1.x/changelog/#version-1-1-x)
  * WTForms 
  * PyMongo
  * slugify
  * bcrypt
  * flask-paginate
6. MongoDB 
7. [Summernote WYSIWYG Editor](https://summernote.org/)
8. [reCAPTCHA](https://www.google.com/recaptcha/about/) 
9. [Materialize CSS](https://materializecss.com/)
10. [Materialize Icons](https://materializecss.com/icons.html)
11. [Google Fonts](https://fonts.google.com/)

## Testing

Please refer to [TESTING.md](bloggy/docs/TESTING.md) for testing documentation

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
| read_time       | Int32
| img_url       | String
| views       | Int32


**user structure**
| Field name       | Data type   
| -------------     |:-------------:| 
| _id               | ObjectId()
| username          | String
| email             | String
| password          | String


### To deploy remotely

I've personally used [Heroku](https://heroku.com/) to deploy this project for submission. The below steps explain how I deployed my app to Heroku. If you're using a different platform to deploy your app, please check and follow relevant documentation.

1. Register for a free account on [Heroku](https://heroku.com/)
2. Create requirements.txt file so they can be installed on Heroku once deployed
* `pip3 freeze --local > requirements.txt`
3. Create Procfile (case sensitive) to inform Heroku what type of application is being deployed
* `echo web: python run.py > Procfile` or alternatively create a Procfile with this line of code using your GUI/IDE.
4. Log into your Heroku account and choose New -> Create new app
5. Input your name (must be unique) and choose region closest to you.
6. After app is created, Heroku will automatically bring you to *Deploy* tab. Under *Deployment Method* choose Github. If you haven't already log into your GitHub account and grant Heroku access to your GitHub data.
7. Type in your repository name and click search, once found, click *Connect*
8. Very imporant part is to declare Config Vars for your app under *Settings* -> *Reveal config vars*
9. Config Vars for this app are:

    | Config Var       | Value   
    | -------------     |:-------------:| 
    | IP               | 0.0.0.0
    | PORT           | 5000
    | DEBUG        | False or True (False for production)
    | MONGO_URI        | Your unique Mongo URI goes here
    | MONGO_DBNAME        | bloggy
    | SECRET_KEY       | Your unique secret key
    | RECAPTCHA_PUBLIC_KEY | Your unique public key supplied by Google
    | RECAPTCHA_PRIVATE_KEY | Your unique private key supplied by Google

## Credits


### Content

__All posts posted on Bloggy are under sole copyright of their respective creators and the creator of this application (Ivan Branimir Skoric) is not responsible for any copyright breaches or foul language that could be contained within users' posts__

### Media

__All images posted on Bloggy are under sole copyright of their respective creators and the creator application (Ivan Branimir Skoric) is not responsible for any copyright breaches that could be commited by other users__

SVG Illustration used in jumbotron have been sourced from [Undraw](https://undraw.co/illustrations). 

Default profile image & default post image sourced from [Pixaby](pixabay.com)

### Acknowledgements

[Tim Nelson](https://github.com/TravelTimN) for his great updated Flask tutorials that he sent me after I posted a question about MongoDB and Flask.
