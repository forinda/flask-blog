from app.models import User, db
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from wtforms import PasswordField, SubmitField, TextAreaField, StringField


class UserCreationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(6, 12)])
    password1 = PasswordField('Confirm', validators=[DataRequired(),
                                                     Length(6, 12), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email taken')

class ProfileUpdate(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    submit = SubmitField('Update profile')

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(6, 12)])
    submit = SubmitField('Login')


class NewBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Add new')


class UpdateBlogForm(FlaskForm):
    title = StringField('Title')
    subtitle = StringField('Subtitle')
    body = TextAreaField('Body')
    submit = SubmitField('Update blog')
