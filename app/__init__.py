from flask import Flask
from app.api_routes import api_bp
from app.extensions import jwt, bcrypt, cors, db
from app.models import *
import cloudinary
import os


def create_app():
    app =  Flask(__name__)
    app.config.from_object("config.DevConfig")

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    cloudinary.config(
        cloud_name=os.environ['CLOUDINARY_CLOUD_NAME'],
        api_key=os.environ['CLOUDINARY_API_KEY'],
        api_secret=os.environ['CLOUDINARY_API_SECRET'],
        secure=True
    )

    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
