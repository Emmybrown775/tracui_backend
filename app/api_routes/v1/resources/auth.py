from flask_jwt_extended import create_access_token
from flask_restx import Namespace, Resource
from flask import request

from app.api_routes.v1.schema.docs import signup_model, check_model
from app.api_routes.v1.schema.forms import SignUpForm
from app.models import User
from app.extensions import db


auth_ns = Namespace("auth", description="Authentication Endpoints")

@auth_ns.route("/")
class Auth(Resource):
    @auth_ns.expect(signup_model)
    def post(self):
        request_json = request.get_json()
        access_token = request_json["access_token"]
        form =  SignUpForm(data=request_json)

        if not form.validate():
            print(form.errors)
            for error in form.errors:
                return {"error": f"{error}:  {form.errors[error][0]}"}, 400

        user = User.query.filter_by(access_token=access_token).first()

        try:

            if user:
                token = create_access_token(user.email, additional_claims={"account_type": user.account_type})
                return {
                    "msg": "user signed in",
                    "data": {"user": {"email": user.email} },
                    "token": token,
                }, 200

            else:
                new_user =  User(
                    access_token=access_token,
                    email=request_json["email"],
                    address=request_json["address"],
                    account_type=request_json["account_type"],
                    private_key=request_json["private_key"],

                )

                db.session.add(new_user)
                db.session.commit()

                token = create_access_token(new_user.email, additional_claims={"account_type": new_user.account_type})
                return {
                    "msg": "user signed in",
                    "data": {"user":{
                        "email": new_user.email
                    }},
                    "token": token,
                }, 201

        except Exception as e:
            return {"error": str(e)}, 500

@auth_ns.route("/check")
class Check(Resource):
    @auth_ns.expect(check_model)
    def post(self):

        email = request.get_json()["email"]

        user = User.query.filter_by(email=email).first()

        if user:
            return {
                "result": True
            }, 200
        else:
            return {
                "result": False
            }














