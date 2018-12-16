from flask import Flask , current_app
from flask_login import UserMixin
from datetime import datetime
from blue import db
from werkzeug.security import generate_password_hash, check_password_hash





class Admin(db.Model):
	__tablename__="admin"
	id=db.Column(db.Integer, primary_key=True)
	admin=db.Column(db.String(50), unique=True)
	password=db.Column(db.String(100))

	def __init__ (self, admin=admin, password=password):
		self.admin=admin
		self.generate_password(password)

	def generate_password(self, password):
		self.password=generate_password_hash(password)
	#def check_password(self, password):
	   # return check_password(self.password, password)
	def check_password(self, password):
		return check_password_hash( self.password, password)

class Peneliti(db.Model):
	__tablename__="peneliti"
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(50))
	email=db.Column(db.String(50))
	password=db.Column(db.String(50))
	universitas=db.Column(db.String(50))
	kategori_penelitian=db.Column(db.String(50))
	jenis_kelamin=db.Column(db.Text)

	def __init__(self, username, email, password, universitas,
                 jenis_kelamin, kategori_penelitian):

		self.username=username
		self.generate_password(password)
		self.email = email
		self.universitas=universitas
		self.kategori_penelitian=kategori_penelitian
		self.jenis_kelamin=jenis_kelamin
		self.authenticated = False
		self.confirmed = False

	def address(self, address):
		self.address=address
	def is_authenticated(self):
		return True
	def is_anonymous(self):
	    return True
	def check_password(self, password):
	    return check_password(self.password, password)
	def is_confirmed(self):
	    return self.confirmed
	def confirm_user(self):
	    self.confirmed = True
	def get_id(self):
	    return str(self.user_id)
	def generate_password(self , password):
	    self.password = generate_password_hash(password)
	def check_password(self , password):
	    return check_password_hash(self.password , password)
	def __repr__(self):
	    return "<User %r>"% (self.nama)


class Petani(db.Model):
	__tablename__="petani"
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(50), unique=True)
	email=db.Column(db.String(50), unique=True)
	password=db.Column(db.String(50))
	address=db.Column(db.String(50))
	kategori_petani=db.Column(db.String(50))
	jenis_kelamin=db.Column(db.Text)

	def __init__(self, username, email, password, address,
                 jenis_kelamin, kategori_petani):
		self.username = username
		self.generate_password(password)
		self.email = email
		self.address=address
		self.kategori_petani=kategori_petani
		self.jenis_kelamin=jenis_kelamin
		self.authenticated = False
		self.confirmed = False
	def is_authenticated(self):
	    return True
	def is_anonymous(self):
	    return True
	def check_password(self, password):
	    return check_password(self.password, password)
	def is_confirmed(self):
	    return self.confirmed
	def confirm_user(self):
	    self.confirmed = True
	def get_id(self):
	    return str(self.user_id)
	def generate_password(self , password):
	    self.password = generate_password_hash(password)
	def check_password(self, password):
	    return check_password_hash(self.password , password)
	def __repr__(self):
	    return "<User %r>"% (self.nama)

class Upload_data(db.Model):
	__upload_data__="upload_data"
	id=db.Column(db.Integer, primary_key=True)
	gambar = db.Column(db.Text)
