from app import app
from flask import redirect, render_template, request, jsonify,session
from flask_marshmallow import Marshmallow
from app.models.userModel import db, Users
from flask_jwt_extended import *
import datetime
from flask import request

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'password', 'role')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def getUser(id):
    user = Users.query.get(id)
    result = user_schema.dump(user)
    return jsonify({"msg": "Success get user by id", "status": 200, "data": result})

def updateUser(id):
    user = Users.query.get(id)
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']

    user.name = name
    user.username = username
    user.setPassword(password)
    db.session.commit()
    result = user_schema.dump(user)
    return user_schema.jsonify({"msg": "Success update user", "status": 200, "data": result})

def signUp():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    
    newUser = Users(name, username)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    user = user_schema.dump(newUser)
    return jsonify({"msg": "Success update users", "status": 200, "data": user})

def signIn():
    username = request.form['username']
    password = request.form['password']

    user = Users.query.filter_by(username=username).first()
    if not user:
        return jsonify("User not found")

    if not user.checkPassword(password):
        return jsonify({
            "status": 401,
            "msg": "Login Invalid",
            "error": "wrong password"
        })
    session["name"] =username
    data = singleTransform(user)
    expires = datetime.timedelta(days=1)
    expires_refresh = datetime.timedelta(days=3)
    access_token = create_access_token(data, fresh=True, expires_delta=expires)
    refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
    newData = {**data, "token": access_token, "refresh_token": refresh_token}
    return redirect("/admin-dashboard")


@jwt_required(refresh=True)
def refresh():
    user = get_jwt_identity()
    new_token = create_access_token(identity=user, fresh=False)

    return jsonify({
        "token_access": new_token
    }, "")

def singleTransform(user):
    return{
        'id': user.id,
        'name': user.name,
        'username': user.username
    }