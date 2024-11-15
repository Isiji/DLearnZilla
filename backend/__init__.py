from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
import os

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'
cors = CORS()
mail = Mail()
jwt = JWTManager()
csrfprotect = CSRFProtect()

def create_app(config_class='config.Config'):
    # Create Flask app instance
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    csrfprotect.init_app(app)
    

    # Register blueprints
    from backend.main.routes import main_bp
    
    
    app.register_blueprint(main_bp)

    return app
