from flask import Flask, render_template, redirect, request, session, logging, url_for 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap 
from flask_wtf import FlaskForm
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///registration.db'
app.config['SECRET_KEY']='thisissupossedtobesecret'
Bootstrap(app)

db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'


class User(UserMixin, db.Model):
	__tablename="User"
	id=db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15) )
	email = db.Column(db.String(50) )
	password = db.Column (db.String(50)) 
	#registered_date=db.Column(db.DateTime)
	role=db.Column(db.Text, default="user")
	job=db.Column(db.String(50))
	address=db.Column(db.String(50))

#class Regis(db.Model):

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int())

class LoginForm(FlaskForm):
	username=StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password=PasswordField('password', validators=[InputRequired(), Length(min=4, max=15)])
	remember=BooleanField('Remember me ya!')

class RegistrationForm(FlaskForm):
	email=StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username=StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password=PasswordField('password', validators=[InputRequired(), Length(min=4, max=15)])
	job=StringField('job', validators=[InputRequired ()])
	address=StringField("address", validators=[InputRequired()])
	role=StringField("role", validators=[InputRequired()])


def Articles():
		articles=[{

			'id':'1',
			'title':'so yeah',
			'body':'yosha man',
			'create_date': '01/11/2018'

		},
		{
			'id':'2',
			'title':'so wew',
			'body':'yahuu',
			'create_date': '01/11/2018'
		},
		{
			'id':'3',
			'title':'so yummy',
			'body':'god',
			'create_date': '01/11/2018'
		}]
		return articles


@app.route('/')
def index():
	return render_template ('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	articles=Articles()
	return render_template('articles.html', articles=articles )

@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id=id )

@app.route('/register', methods=['GET', 'POST'])
def register():
	form=RegistrationForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(
			username=form.username.data, 
			email=form.email.data, 
			password =hashed_password,
			job=form.job.data,
			address=form.address.data
			)
		db.session.add(new_user)
		db.session.commit()

		#return render_template(url_for('/'))
		return '<h1>' +' new user has been created god'+ '</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>' 
	return render_template('register_agri.html',form=form)

@app.route('/login',methods=["GET", "POST"])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.username.data).first()
		if user and check_password_hash(user.password, form.password.data):
			if user.role=='admin' :
				return redirect(url_for('articles'))
		else:		
			return render_template ('after_login.html')
			#login_user(user)
			#if user.role=='admin' :
				#return redirect(url_for('articles'))

			

				
		return '<h1> Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
	return render_template('login.html', form=form)


@app.route('/logout')
def logout():
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)


###################################################
############# ADMIN AREA   ########################
###################################################


admin=Admin(app)
admin.add_view(ModelView(User, db.session))