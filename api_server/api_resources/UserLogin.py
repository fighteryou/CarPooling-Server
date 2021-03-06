from flask import request, jsonify
from flask_restful import Resource
from ..forms import LoginForm
from ..database import User


class UserLogin(Resource):
    """
        this is the API for user login
    """

    def post(self):
        form = LoginForm.from_json(request.get_json())
        error_messages = []
        if form.validate_on_submit():
            user = User.query.filter_by(name=form.name.data).first()
            if user and user.verify_password(form.password.data):
                token = user.generate_auth_token()
                info = {}
                info['name'] = user.name
                info['email'] = user.email
                info['phone'] = user.phone
                info['photo'] = user.photo
                list = []
                list.append(str(info))
                return jsonify({"status": True, "token": token.decode("ascii"), "message": list})
            elif not user:
                error_messages.append("User not exist")
                return jsonify({"status": False, "message": error_messages})
            else:
                error_messages.append("Wrong password")
                return jsonify({"status": False, "message": error_messages})
        else:
            error_messages = [form.errors[n] for n in form.errors][0]
            return jsonify({"status": False, "message": error_messages})
