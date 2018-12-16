from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from blue.models_database import Peneliti
from bluen import db


bp=Blueprint('peneliti',__name__,
				templates_folder='templates',
				static_folder='static')


@bp.route("/login/peneliti", methods=["GET","POST"])
#@login_required
def login_peneliti():
    if request.method=="POST":
    	email=request.form["username"]
    	password=request.form["password"]
    	user=Peneliti.query.filter_by(username=username).first()
    	if user and user.check_password(password):
    		#load_user_peneliti(user)
    		return redirect(url_for("page_market_place"))
    return render_template("login_peneliti.html")

@bp.route("/market_page")
def market_page():
	return "<h1> you are in market page right now </h1>"

@bp.route("/register/peneliti", methods=["GET", "POST"])
def register_peneliti():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        universitas=request.form["universitas"]
        kategori_penelitian=request.form.get('kategori penelitian')
        jenis_kelamin = request.form.get("jenis kelamin")
        if not Peneliti.query.filter_by(username=username).first():

            user = Peneliti(username=username, email=email, kategori_penelitian=kategori_penelitian, 
            			universitas=universitas,
                        jenis_kelamin=jenis_kelamin, 
                         password=password)

            db.session.add(user)
            db.session.commit()
            return "<h1> your registration as researcer has been accepted, please login </h1>"

    return render_template("register_peneliti.html")
