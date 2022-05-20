from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import timedelta


db = SQLAlchemy()
app = Flask(__name__)
DB_NAME = "database.db"



def create_app():
	app.config['SECRET_KEY'] = 'CHARLOSYANGBUAT'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	app.config['IMAGE_UPLOAD'] = "D:/Belajar/Belajar/Kelas 11/Semester 2/Tugas/website/static/img/user_upload" #Ubah dewek file path nyo
	
	app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG','JPG','JPEG']
	app.config['MAX_IMAGE_FILESIZE'] = 0.5*1024*1024


	db.init_app(app)

	from .views import views
	from .auth import auth


	app.register_blueprint(views,url_prefix='/')
	app.register_blueprint(auth,url_prefix='/')

	from .models import User 

	create_database(app)

	login_manager = LoginManager()
	login_manager.login_view = "auth.login"
	app.permanent_session_lifetime = timedelta(hours=2)
	login_manager.init_app(app)


	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists('website/'+DB_NAME):
		db.create_all(app=app)
		print('Created Database!')

