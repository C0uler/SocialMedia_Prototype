# Flask Things
from flask import Blueprint,render_template,request,redirect,url_for,flash,session,jsonify
from flask_login import login_required,current_user

# Data From Other File
from .models import User
from . import db,app
from .forms import RegistarationForm,LoginForm

# Anything else
import os
from werkzeug.utils import secure_filename


views = Blueprint('views',__name__)

@views.route("/",defaults={'ids':'charlos'})
@views.route("//<ids>")
def home(ids):

	users = User.query.filter_by(username=ids).first()

	return render_template('normal_index.html',ids = ids,user=current_user,users = users)

@views.route("/profile",defaults={'ids':'charlos','custumize':'False','edit':'False'})
@views.route("/profile/<ids>/<custumize>/<edit>",methods=['GET','POST'])

def profile(ids,custumize,edit):
	all_user = User.query.order_by('username')
	userss = all_user
	if request.method == 'POST':	
		userss = []
		search = request.form.get('Search')
		
		if search == None:
			pass
		else:
			for alls in all_user:
				if search in alls.username:
					userss.append(alls)	
	try: 
		a = current_user.id
	except Exception:
		return redirect(url_for('auth.login'))
	else:
		return render_template('user_index.html',user=current_user,ids = ids,custumize=custumize,edit=edit,all_user=userss)

def allowed_image(filename):

	if not "." in filename:
		return False

	ext = filename.rsplit(".",1)[1]
	secure = secure_filename(filename)

	if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS'] and secure:
		return True
	else:
		return False

# def allowed_image_filesize(filesize):

# 	if int(filesize) <= app.config['MAX_IMAGE_FILESIZE']:
# 		return True

# 	return False



@views.route('/update',defaults={'edit':False})
@views.route('/update/<edit>',methods=['GET','POST'])
@login_required
def update(edit):
	user = User.query.filter_by(id=current_user.id).first()
	if request.method == 'POST':
		if edit.lower() == 'login_update':
			data = request.form.get('logo_name')
			
			if len(data) <= 20:
				user.data_logo = data
				db.session.add(user)
				db.session.commit()
				flash('Data Updated',category='success')
				
			else:
				
				flash('Maximum length is 20',category='error')

			
		elif edit.lower() == 'username_input':
			data = request.form.get('username')

			if request.files:	
				image = request.files['image']
				if image:

					if allowed_image(image.filename):

						image.save(os.path.join(app.config["IMAGE_UPLOAD"], image.filename))

						user.image_username = 'img/user_upload/' + image.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')
			
			if len(data) <= 20 and len(data) >= 1:
				user.data_name = data
				db.session.add(user)
				db.session.commit()
				flash('Data Updated',category='success')

				
			else:
				
				flash('Maximum length is 20',category='error')

		elif edit.lower() == 'about1_edit':
			data = request.form.get('about1')
			
			if len(data) <= 2000:
				user.data_about1 = data
				db.session.add(user)
				db.session.commit()
				flash('Data Updated',category='success')
				
			else:
				flash('Maximum length is 2000',category='error')

		elif edit.lower() == 'about2_edit':
			data = request.form.get('about2')

			if len(data) <= 2000:
				user.data_about2 = data
				db.session.add(user)
				db.session.commit()
				flash('Data Updated',category='success')
				
			else:
				flash('Maximum length is 2000',category='error')

		elif edit.lower() == 'projects_edit':
			
			if request.files:	
				image_1 = request.files['image_project1']
				image_2 = request.files['image_project2']
				image_3 = request.files['image_project3']
				image_4 = request.files['image_project4']
				image_5 = request.files['image_project5']

				if image_1:
					if allowed_image(image_1.filename):
						image_1.save(os.path.join(app.config["IMAGE_UPLOAD"], image_1.filename))

						user.image_project1 = 'img/user_upload/' + image_1.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image For Project 1 Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')

				if image_2:
					if allowed_image(image_2.filename):
						image_2.save(os.path.join(app.config["IMAGE_UPLOAD"], image_2.filename))

						user.image_project2 = 'img/user_upload/' + image_2.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image For Project 2 Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')

				if image_3:
					if allowed_image(image_3.filename):
						image_3.save(os.path.join(app.config["IMAGE_UPLOAD"], image_3.filename))

						user.image_project3 = 'img/user_upload/' + image_3.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image For Project 3 Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')

				if image_4:
					if allowed_image(image_4.filename):
						image_4.save(os.path.join(app.config["IMAGE_UPLOAD"], image_4.filename))

						user.image_project4 = 'img/user_upload/' + image_4.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image For Project 4 Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')

				if image_5:
					if allowed_image(image_5.filename):
						image_5.save(os.path.join(app.config["IMAGE_UPLOAD"], image_5.filename))

						user.image_project5 = 'img/user_upload/' + image_5.filename
						db.session.add(user)
						db.session.commit()
					else:
						flash("Image For Project 5 Not Uploaded Input Just ['JPG','JPEF','PNG']",category='error')



	return redirect(url_for('views.profile',ids='charlos',custumize='true',edit='false'))


@views.route('/searchs',defaults={'user':None})
@views.route('/searchs/<user>',methods=['POST','GET'])
# @login_required
def searchs(user=None):
	all_user = User.query.order_by('username')
	userss = all_user
	
	if user == 'null':
		pass
	# if request.method == 'POST':	
	else:
		userss = []
		for alls in all_user:
			if user in alls.username:
				userss.append(alls)	
	
	return jsonify('',render_template('search_index.html',all_user = userss, user = current_user.username))


	
	




