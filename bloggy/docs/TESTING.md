# Bloggy - The home of blogs you love

![Bloggy logo](../static/img/logo.svg "Bloggy logo Logo")

## Testing

## Table of Contents
1. [**Testing**](#testing)
    - [**Home page and posts displaying**](#🛠-home-page-and-posts-displaying)
    - [**Home page and posts searching**](#🛠-home-page-and-posts-searching)
    - [**Home page posts sorting**](##🛠-home-page-posts-sorting)
    - [**Registration form**](#🛠-registration-gorm)
    - [**Login form**](#🛠-login-form)
    - [**Write a new post form**](#🛠-write-a-new-post-form)
    - [**Read a single post**](#🛠-read-a-single-post)
    - [**Edit a post**](#🛠-edit-a-post)
    - [**Delete a post**](#🛠-delete-a-post)

### 🛠 Home page and posts displaying

Once home page loads, users are presented with all posts on Bloggy. First 6 posts are present on page with pagination displayed at the bottom of the page for navigation to more posts.

If the user is logged in, underneath their posts, alongside read link, edit and delete links will be displayed. Similarly if admin user is logged in, edit and delete links will display for all posts.

### 🛠 Home page and posts searching

MongoDB text search is utilised to search the database based on user's query. Indexes are set up for *title*, *description* & *body* fields - hence, users can search for posts based on title, description or tags. 

By clicking on the cancel button, user is returned back to the index page.

If the user is logged in, underneath their posts, alongside read link, edit and delete links will be displayed. Similarly if admin user is logged in, edit and delete links will display for all posts.

Note that MongoDB is automatically ignoring 'stop' words, more on which can be read [here](https://docs.mongodb.com/manual/reference/operator/query/text/#stop-words). These can be disabled by creating an index but I've chosen not to disable them.

### 🛠 Home page posts sorting

Users are able to sort posts by date created (Most recent first/Oldest first), alphabetically (A-Z/Z-A) & by popularity by clicking on dropdown select menu under search field.

If users chooses to sort by most recent first, filter on database query is utilised to filter it by *last_updated* in descending order.

Similarly for oldest first, database query is utilised to filter it by *last_updated* in ascending order.

To sort by popularity, database query is used to filter results by *views* which is also displaying on post cards next to read time.

### 🛠 Registration form

WTForms validators are used to validate all forms on the site along some custom checks (ie. if the username exists in the database or not etc.)

All validators used in the registration form can be seen in `forms.py` file and more about WTForms validators can be read about [here](https://wtforms.readthedocs.io/en/2.3.x/validators/)

If the validation of any of the fields fails on submit, a message will be displayed under the field in red text. 

If the validation is successful user's details - username, email, password and profile picture are stored in the users collection & their blog title and description are stored in the blogs collection.

Once user is successfully registered they are redirected to the login form with a flash message informing them they've been successfully registered.

### 🛠 Login form

Similarly to the [registration form](#registration-form), WTForms is used to preform validation checks of the form. 

All validators used in the registration form can be seen in `forms.py` file.

If the validation of any of the fields fails on submit, a message will be displayed under the field in red text. 

Users details - username and password are compared to the ones in the database (password hash is checked using [bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)). If the details match user will be brought to their user page with flash message informing them they've been successfully logged in. If the details do not match, flash message will display "Details incorrect".

### 🛠 User/profile page 

User/profile page displays user's profile photo, blog title and blog description. Underneath that, user's posts are displayed. 

Users are able to sort posts - refer to [**Home page posts sorting**](##🛠-home-page-posts-sorting) section for explanation and details.

If the user that's logged in is viewing their own profile, underneath their posts, alongside read link, edit and delete links will be displayed. Similarly if admin user is logged in, edit and delete links will be displayed.

### 🛠 Edit profile

Logged in users are able to edit their profiles - more specifically their password and their blog description. 

Users are able to access this page by clicking *Edit Profile* button on their profile page. 

Should an anonymous user try and access the `/user/edit` page, they will be redirected to the home page with a flash message reading *You must be logged in to access this page*

In this case, WTForms is used to create the form but the form itself is validated manually to give the user to either just change the blog description, just the password or both at one time. 

If the user's current password doesn't match one stored in the database a message reading *Current password is not correct* will be displayed. 

If the user inputs correct password but leaves the new password fields empty, a message reading *You entered your existing password but not the new password. Please check your fields and try again.*


### 🛠 Write a new post form

Once again, WTForms is used to validate form on this page, all validators used in the registration form can be seen in `forms.py` file.

If the validation of any of the fields fails on submit, a message will be displayed under the field in red text. 

Should an anonymous user try and access the `/user/new_post` page, they will be redirected to the login page with a flash message reading *You must be logged in to create a new post*

### 🛠 Read a single post

By clicking *Read* on the post card user will be brought to the `/post/<post_id>` page where, by using post ID, post title, image, body and author details will be pulled from the database. Reader is able to visit author's profile by clicking on *Visit their profile* link under the author's name.

### 🛠 Edit a post

*Edit* option will only appear on the post card if the user is logged in as the creator of the post or if the logged in user is admin. By clicking on the edit link user is essentially brought back to the pre-populated 'New post" page where they are able to edit any post data they like. 

WTForms is used to validate form on this page, all validators used in the registration form can be seen in `forms.py` file.

If the validation of any of the fields fails on submit, a message will be displayed under the field in red text. 

Should an anonymous user try and access the `/post/<post_id>/edit` page, they will be redirected to the home page with a flash message reading *You don't have permission to edit this post*

### 🛠 Delete a post

*Delete* option will only appear on the post card if the user is logged in as the creator of the post or if the logged in user is admin. By clicking on the delete link, a modal is displayed to the user prompting them to confirm the deletion of the post and warning them that that action cannot be undone. 

If the user click's *Delete* the modal will disappear and the post will be deleted. If the user click's cancel, the modal will disappear but the post will not get deleted. 

Should an anonymous user try and access the `/post/<post_id>/delete` page, they will be redirected to the home page with a flash message reading *You don't have permission to delete this post*









