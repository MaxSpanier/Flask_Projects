from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)

    from app.navbar_hacking import bp as navbar_hacking_bp
    app.register_blueprint(navbar_hacking_bp)
    
    from app.picture_hover_snake import bp as picture_hover_snake_bp
    app.register_blueprint(picture_hover_snake_bp)
    
    from app.camillemormal_clone import bp as camillemormal_clone_bp
    app.register_blueprint(camillemormal_clone_bp)

    return app
