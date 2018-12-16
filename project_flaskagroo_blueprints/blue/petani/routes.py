from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from blue.models_database import Petani



bp=Blueprint('petani',__name__,
                templates_folder='templates',
                static_folder='static')



@bp.route("/login/petani", methods=["GET","POST"])
def login_petani():
    if request.method=="POST":
    	username=request.form["username"]
    	password=request.form["password"]
    		
    	user=Petani.query.filter_by(username=username).first()
    	if user  and user.check_password(password) :
    		#user.is_authenticated = True

    		#load_user_petani(user)
    		return redirect(url_for("dashboard_login_petani"))
    return render_template("login_petani.html", title="Petani Login")

@bp.route('/dashboard_login_petani')
#@login_required
def dashboard_login_petani():
    return render_template ("dashboard_login_petani.html")



@bp.route("/register/petani", methods=["GET", "POST"])
def register_petani():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        kategori_petani=request.form.get("kategori petani")
        address=request.form['address']
        jenis_kelamin=request.form.get('jenis kelamin')
        if not Petani.query.filter_by(username=username).first():

            user = Petani(username=username, email=email, address=address, jenis_kelamin=jenis_kelamin, 
                         kategori_petani=kategori_petani,
                         password=password)

            db.session.add(user)
            db.session.commit()
            return "<h1> your registration has been accepted, please login</h1>"   

    return render_template("register_petani.html")