from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo, Email
from dWo.models import User

class FormSignUp(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_add=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='Username:',validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
