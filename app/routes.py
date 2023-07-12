from flask.templating import render_template
from app import app
from flask import request, redirect, session
from app.controllers import modelController, tokohController, updateDataController, authController

@app.route("/buatModel", methods=['POST', 'GET'])
def buatModel():
    if not session.get("name"):
        return redirect("/admin-login")
    if(request.method == 'POST'):
        return modelController.createModel()
    elif(request.method == 'GET'):
        return render_template('createModel.html')

@app.route("/updateData", methods=['PUT', 'GET'])
def updateData():
    if not session.get("name"):
        return redirect("/admin-login")
    if(request.method == 'PUT'):
        return updateDataController.update()
    elif(request.method == 'GET'):
        return updateDataController.getAllTokoh()
    
@app.route('/v1/admin-register', methods=['POST'])
def signUp():
    if request.method == 'GET':
        print("melihat semua user")
    elif request.method == 'POST':
        return authController.signUp()
    
@app.route('/admin-login', methods=['POST', 'GET'])
def signIn():
    if(request.method == 'GET'):
        return render_template('login.html')
    elif(request.method == 'POST'):
        return authController.signIn()

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/admin-login")

@app.route("/admin-dashboard", methods=['GET'])
def index():
    if not session.get("name"):
        return redirect("/admin-login")
    return tokohController.getAllTokoh()
    
@app.route("/tokoh/<id>")
def tokohById(id):
    return tokohController.getDetailTokoh(id)

@app.route("/hapusTokoh/<id>")
def deleteTokoh(id):
    return tokohController.deleteTokoh(id)


@app.route("/", methods=['GET'])
def sentiment():
    return tokohController.getAllTokohUser()

@app.route("/tokohs/<id>")
def tokohByIds(id):
    return tokohController.getDetailTokohUser(id)
