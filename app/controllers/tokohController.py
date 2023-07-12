from flask import request, jsonify, redirect, flash
from flask.templating import render_template
from app import app
from app.models.dataTokohModel import db, Tokoh
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class TokohSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama', 'positif', 'negatif', 'netral', 'akurasi', 'image', 'update_at')

tokoh_schema = TokohSchema()
tokohs_schema = TokohSchema(many=True)

def getAllTokoh():
    konten = Tokoh.query.all()
    tokos= tokohs_schema.dump(konten)
    images = Tokoh.query.all()
    imagess= tokohs_schema.dump(images)
    print(tokos)
    return render_template('index.html', data = tokos,image = imagess)
    
def getDetailTokoh(id):
    konten = Tokoh.query.get(id)
    kontens = tokoh_schema.dump(konten)
    images = Tokoh.query.all()
    imagess= tokohs_schema.dump(images)
    print(kontens)
    return render_template("index.html", data= kontens, image = imagess)
    # con = tokohs_schema.dump(konten)
    # return jsonify (con)


def updateTokoh(id):
    tokoh = Tokoh.query.get(id)
    nama = request.form['nama']
    nama = request.form['nama']
    positif = request.form['positif']
    negatif = request.form['negatif']
    netral = request.form['netral']
    akurasi = request.form['akurasi']

    tokoh.nama = nama
    tokoh.positif = positif
    tokoh.negatif = negatif
    tokoh.netral = netral
    tokoh.akurasi = akurasi

    db.session.commit()
    tokohUpdate = tokoh_schema.dump(tokoh)
    return jsonify({"msg": "Success update tokoh", "status": 200, "data": tokohUpdate})

def getAllTokohUser():
    konten = Tokoh.query.all()
    tokos= tokohs_schema.dump(konten)
    images = Tokoh.query.all()
    imagess= tokohs_schema.dump(images)
    print(tokos)
    return render_template('users.html', data = tokos,image = imagess)
    
def getDetailTokohUser(id):
    konten = Tokoh.query.get(id)
    kontens = tokoh_schema.dump(konten)
    images = Tokoh.query.all()
    imagess= tokohs_schema.dump(images)
    print(kontens)
    return render_template("users.html", data= kontens, image = imagess)

def deleteTokoh(id):
    tokoh = Tokoh.query.get(id)
    db.session.delete(tokoh)
    db.session.commit()
    flash('Tokoh Berhasil Dihapus!')
    # tokohDelete = tokohs_schema.dump(tokoh)
    return redirect ('/updateData')
