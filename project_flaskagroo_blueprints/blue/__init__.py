from flask import Flask, Blueprint 
from flask_sqlalchemy import SQLAlchemy
from blue.admin.routes import bp 
from blue.petani.routes import bp 
from blue.peneliti.routes import bp




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///agreed.db'
app.config['SECRET_KEY']='thisissupposedtobesecret'




db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    
    app.register_blueprint(admin.routes.bp)
    app.register_blueprint(petani.routes.bp)
    app.register_blueprint(peneliti.routes.bp)

    return app
