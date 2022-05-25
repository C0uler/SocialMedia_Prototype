from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistarationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=8,message='you stupid')])
	confirm_password = PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('SignUp')

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	password = StringField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')



