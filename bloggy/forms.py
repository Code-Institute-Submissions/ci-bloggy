import re
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired, Email, EqualTo, ValidationError, URL
from bloggy.utilities import check_username, existing_email, existing_blog
from slugify import slugify
from bloggy import bcrypt

class RegisterForm(FlaskForm):
    def username_check(form, username):
        specials = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        if specials.search(username.data) != None:
            raise ValidationError('You cannot use special charachters such as [@_!#$%^&*()<>?/\|}{~:] in your username')
        if check_username(form.username.data):
            raise ValidationError('User with such username already exists, please choose a different one')
        
    def check_existing_blog(form, blog_title):
        if existing_blog(slugify(form.blog_title.data)):
            raise ValidationError('Great idea, but the blog whith such name already exists')
        
    def check_existing_email(form, email):
        if existing_email(form.email.data):
            raise ValidationError("This email address is already in use, please choose a different one")
    
    username = StringField(
        'username', validators=[DataRequired(), 
                                Length(min=5, max=35, message="Username should be between 5 and 35 charachters long"), 
                                InputRequired(message="This field is requried"), username_check])
    email = StringField(
        'email', validators=[DataRequired(), 
                             Email(), 
                             InputRequired(message="This field is requried"), check_existing_email])
    blog_title = StringField(
        'blog_title', validators=[DataRequired(), 
                                        Length(min=5, max=35), 
                                        InputRequired(message="This field is requried"), check_existing_blog])
    blog_description = StringField(
        'blog_description', validators=[DataRequired(), 
            Length(min=5, max=200), 
            InputRequired(message="This field is requried")])
    password = PasswordField(
        'password', validators=[DataRequired(), 
            Length(min=5, max=35), 
            InputRequired(message="This field is requried")])
    confirm_password = PasswordField(
        'confirm_password', validators=[DataRequired(),
                                       EqualTo('password', message="Passwords must match"),
                                       InputRequired(message="This field is requried")])
    recaptcha = RecaptchaField()
    
class LoginForm(FlaskForm):
    def username_validation(form, username):
        if check_username(form.username.data) is None:
            raise ValidationError('User with such username does not exist')
            
    username = StringField(
        'username', validators=[DataRequired(),
                                Length(min=5, max=35, message="Username should be between 5 and 35 charachters long"),
                                InputRequired(message="This field is requried"), username_validation])
    password = PasswordField(
        'password', validators=[
            DataRequired(), 
            InputRequired(message="This field is requried")])
    
class NewPostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(),
                                Length(min=5, max=150, message="Title should be at least 5 letters long"),
                                InputRequired(message="This field is requried")])
    image_url = StringField('image_url', validators=[DataRequired(),
                                URL(message="Please input a valid URL"),
                                InputRequired(message="This field is requried")])
    