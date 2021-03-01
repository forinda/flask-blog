from flask import (
    Flask, 
    flash, 
    render_template, 
    session, 
    url_for
    )
from flask_login import (
    LoginManager, 
    login_required, 
    login_user, 
    current_user,
    logout_user
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config

app = Flask(__name__)
app.config.from_object(config['production'])
db = SQLAlchemy(app)
migrate = Migrate(app)
login_manager = LoginManager(app)


login_manager.login_message = 'You need to login to access this page'
login_manager.login_view = 'home.sign_in'
login_manager.login_message_category = 'danger'


from app.views import home

app.register_blueprint(home)
