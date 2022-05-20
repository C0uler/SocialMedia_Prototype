# Import dari flask
from flask import Blueprint,render_template,redirect,request,flash,url_for
from flask_login import login_user, login_required, logout_user,current_user

# Import dari file lain
from .models import User
from .forms import RegistarationForm,LoginForm
from .import db

# import dari device
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)


@auth.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = None
		username = form.username.data
		password = form.password.data
		email = form.username.data
		print(username)
		user_by_Username = User.query.filter_by(username=username).first()
		user_by_email = User.query.filter_by(email_address=email).first()

		if user_by_Username:
			user = user_by_Username
		elif user_by_email:
			user = user_by_email

		if user:
			if check_password_hash(user.password,password):
				flash('Logged in succesfully!',category='success')
				login_user(user,duration = timedelta(seconds=1))
				return redirect(url_for('views.profile'))
			else:
				flash('Incorrect password, try again.',category='error')
		else:
			flash("Email does not exist.",category='error')
		
	return render_template('login_page.html',form = form)

@auth.route('/SignUp',methods = ['GET','POST'])
def SignUp():
	form = RegistarationForm()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		email = form.email.data
		user = User.query.filter_by(username=username).first()
		if username != "null" or username != None:

		
			if user is None:
				user = User.query.filter_by(email_address=email).first()
				if user is None:	
					new_user = User(username = username,password=generate_password_hash(password,method='sha256'),email_address=email)
					db.session.add(new_user)
					db.session.commit()
					login_user(new_user,duration = timedelta(seconds=1))
					return redirect(url_for('views.profile'))
				else:
					flash('email address already exist',category='error')
			else:
				flash('username already exist',category='error')
		else:
			flash('congratulation you find the bug',category='error')


				
	return render_template('sign_up.html',form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	# return redirect(url_for('auth.login'))
	flash('Logout Succesfully',category='success')
	return redirect(url_for('views.home'))

@auth.route('/password_loss')
def password_loss():
	return render_template('password_loss.html')

@auth.route('/fde')
def fde():
	return render_template('feature_doesnt_exist.html')
