from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), 
                                Length(min=5, max=35, message="Username should be between 5 and 35 charachters long"), 
                                InputRequired(message="This field is requried")])
    email = StringField(
        'email', validators=[DataRequired(), 
                             Email(), 
                             InputRequired(message="This field is requried")])
    blog_title = StringField(
        'blog_title', validators=[DataRequired(), 
                                        Length(min=5, max=35), 
                                        InputRequired(message="This field is requried")])
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
    username = StringField(
        'username', validators=[DataRequired(), 
                                Length(min=5, max=35, message="Username should be between 5 and 35 charachters long"), 
                                InputRequired(message="This field is requried")])
    password = PasswordField(
        'password', validators=[
            DataRequired(), 
            Length(min=5, max=35, message="Username should be between 5 and 35 charachters long"), 
            InputRequired(message="This field is requried")])