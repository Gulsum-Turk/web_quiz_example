# models.py
from . import db, app



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(10), nullable=False)

class Sinav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adi = db.Column(db.String(100))
    aciklama = db.Column(db.Text)
    sorular = db.relationship('Soru', backref='sinav', lazy=True)
    def __repr__(self):
        return f'<Card {self.id}>'

class Soru(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icerik = db.Column(db.Text)
    dogru_cevap = db.Column(db.String(100))
    secenek1 = db.Column(db.String(100))
    secenek2 = db.Column(db.String(100))
    secenek3 = db.Column(db.String(100))
    secenek4 = db.Column(db.String(100))
    sinav_id = db.Column(db.Integer, db.ForeignKey('sinav.id'), nullable=False)
    def __repr__(self):
        return f'<Card {self.id}>'

class LeaderTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adi = db.Column(db.String(100))
    puan = db.Column(db.Integer, default=0)
    def __repr__(self):
        return f'<Card {self.id}>'


with app.app_context():
    db.create_all()