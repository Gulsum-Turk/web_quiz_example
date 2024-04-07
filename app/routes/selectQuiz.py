from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import Sinav
from app.models import Soru

@app.route('/select', methods=['GET'])
def sinav_sec():
    logged_in = True
    username = session['username']
    sinavlar = Sinav.query.all()
    return render_template("selectQuiz.html", sinavlar=sinavlar, logged_in=logged_in, username=username)



@app.route('/select', methods=["POST"])
def sinav_sil():
    if request.method == "POST":
        number = request.form['number']
        silineceksinav = Sinav.query.filter_by(id=number).first()  # İlk eşleşen öğeyi al
        silineceksoru = Soru.query.filter_by(id=number).first()  # İlk eşleşen öğeyi al
         # Silinecek bir öğe varsa
        if silineceksoru:
            db.session.delete(silineceksoru)
        if silineceksinav:
            db.session.delete(silineceksinav)
        db.session.commit()
    sinavlar = Sinav.query.all()  # Silindikten sonra güncellenmiş sınav listesini al
    return render_template("selectQuiz.html", sinavlar=sinavlar)
