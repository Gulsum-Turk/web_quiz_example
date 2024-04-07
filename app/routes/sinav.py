from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import Sinav
from app.models import Soru
import random





@app.route('/sinav/<sinav_id>', methods=['POST', 'GET'])
def sinav_ol(sinav_id):
    logged_in = True
    username = session['username']
    dizi={}
    sinav = Sinav.query.get(sinav_id)
    
    
    print(sinav.id)
    for soru in sinav.sorular:
            dizi[soru]=[]
            dizi[soru].append(soru.dogru_cevap)
            dizi[soru].append(soru.secenek1)
            dizi[soru].append(soru.secenek2)
            dizi[soru].append(soru.secenek3)
            dizi[soru].append(soru.secenek4)
            random.shuffle(dizi[soru])





    return render_template('sinav.html', sinav=sinav, cevap=dizi, logged_in=True, username=username )