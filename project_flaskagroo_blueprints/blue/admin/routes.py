from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from blue.models_database import Admin



bp=Blueprint('admin',__name__,
				templates_folder='templates',
				static_folder='static')


@bp.route('/login/admin', methods=["GET", "POST"])
#@login_required
def login_admin():
	if request.method=="POST":
		admin=request.form['admin']
		password=request.form['password']
		user=Admin.query.filter_by(admin=admin).first()
		if user and user.check_password(password):
			return redirect(url_for('dashboard_admin'))
	return render_template ('login_admin.html')

@bp.route('/dashboard_admin')
def dashboard_admin():
	return "<h1> you are in controller page </h1>"



