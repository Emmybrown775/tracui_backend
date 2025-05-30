from flask_restx import Api, Resource, fields, reqparse
from app.extensions import api



signup_model = api.model('SignUp', {
    'access_token': fields.String(required=True, description='The user\'s email address'),
    'access_secret': fields.String(description='The user\'s email address'),
    'email': fields.String(required=True, description='The user\'s password'),
    'address': fields.String(required=True, description='The user\'s username'),
    'account_type': fields.String(required=True, description='The user\'s gender'),
})

check_model = api.model("Check", {
    "email": fields.String(required=True, description="The user's email")
})



