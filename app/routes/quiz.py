from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import Sinav
from app.models import Soru



@app.route('/sinav_ekle', methods=['POST', "get"])
def sinav_ekle():
    if request.method == 'POST':
        sınav_adı = request.form['sınav_adı']
        sınav_aciklama = request.form['sınav_aciklama']

        yeni_sinav = Sinav(adi=sınav_adı, aciklama=sınav_aciklama)
        db.session.add(yeni_sinav)
        db.session.commit()

        for i in range(1, 4):  # 3 soru ekleyelim
            soru_icerik = request.form[f'soru{i}']
            dogru_cevap = request.form[f'dogru_cevap{i}']
            secenek1 = request.form[f'secenek{i}_1']
            secenek2 = request.form[f'secenek{i}_2']
            secenek3 = request.form[f'secenek{i}_3']
            secenek4 = request.form[f'secenek{i}_4']

            yeni_soru = Soru(icerik=soru_icerik, dogru_cevap=dogru_cevap, secenek1=secenek1,
                         secenek2=secenek2, secenek3=secenek3, secenek4=secenek4, sinav_id=yeni_sinav.id)
            db.session.add(yeni_soru)
            db.session.commit()
        return "sınav başarılı şekilde oluşturuldu"
    else:
        return render_template("quiz.html")
