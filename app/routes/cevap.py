from flask import request, redirect, url_for, session, render_template
from app import app, db
from app.models import Sinav
from app.models import Soru
from app.models import LeaderTable



@app.route('/cevap', methods=['POST'])
def cevap():
    if request.method == 'POST':
        # Kullanıcının seçtiği cevapları alalım
        cevaplar = {}
        for key, value in request.form.items():
            if key.startswith('soru'):
                cevaplar[int(key[4:])] = value

        # Burada cevapları kontrol edip puan hesaplama işlemleri yapılabilir.
        # Örneğin, her bir doğru cevap için 5 puan verilebilir.
        puan = 0
        for soru_id, secilen_cevap in cevaplar.items():
            soru = Soru.query.get(soru_id)
            if soru and secilen_cevap == soru.dogru_cevap:
                puan += 5

        # Puanı veritabanına kaydet
        # Örnek olarak, kullanıcı oturumu üzerinden kullanıcı adını alalım
        kullanici_adi = session.get('username')

        if kullanici_adi:
            kullanici = LeaderTable.query.filter_by(adi=kullanici_adi).first()
            if kullanici:
                kullanici.puan += puan
            else:
                newPlace = LeaderTable(adi=kullanici_adi, puan=puan)
                db.session.add(newPlace)
            db.session.commit()

        # Son olarak, kullanıcıyı bir sonraki sayfaya yönlendir
        return render_template("cevap.html", puan=puan)

    # GET isteği yapıldığında cevap vermek istiyorsanız, aşağıdaki kodu ekleyebilirsiniz
    return render_template("cevap.html", puan=None)

