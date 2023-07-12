from datetime import datetime
from app import db

class Tokoh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    positif = db.Column(db.String(100), nullable=True)
    negatif = db.Column(db.String(100), nullable=True)
    netral = db.Column(db.String(100), nullable=True)
    akurasi = db.Column(db.String(100), nullable=True)
    image = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    update_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __init__(self, nama, akurasi, image):
        self.nama = nama
        self.akurasi = akurasi
        self.image = image