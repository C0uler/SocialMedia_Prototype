from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(150), unique = True)
	email_address = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	data_logo = db.Column(db.String(30),default="Charlos Ferdinand")
	data_name = db.Column(db.String(20),default='Jordan')
	data_about1 = db.Column(db.String(2000),default='Saya lahir di kota Palembang, dan merupakan seorang siswa di sekolah SMA Ignatius Global School (IGS).')
	data_about2 = db.Column(db.String(2000),default="I'm from Palembang, Indonesia and is a student of IGS as of 2022 learning about coding and etc.")
	image_username = db.Column(db.String(2000),default="img/gambar_anjing.jfif")
	image_project1 = db.Column(db.String(2000),default="img/foto2.png")
	image_project2 = db.Column(db.String(2000),default="img/foto3.png")
	image_project3 = db.Column(db.String(2000),default="img/foto4.png")
	image_project4 = db.Column(db.String(2000),default="img/foto5.png")
	image_project5 = db.Column(db.String(2000),default="img/foto6.png")
	