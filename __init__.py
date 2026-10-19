from flask import Flask
from app.config import Config
from app.routes.student_routes import student_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(student_bp)

    return app