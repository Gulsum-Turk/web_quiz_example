from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import User



# Giriş sayfası
@app.route('/login', methods=["get","post"])
def login():
    if request.method == 'POST':
    #formdan gelen bilgiler
        formName = request.form['name']
        formPassword = request.form['password']
    #veri tabanından gelen bilgiler
        user = User.query.filter_by(userName=formName).first()

        if user:  # Kullanıcı veritabanında varsa
            if user.password == formPassword:  # Parolalar eşleşiyorsa
            # Başarılı giriş, burada kullanıcıyı ana sayfaya yönlendirin veya başka bir işlem yapın
                session['username'] = user.userName
                return redirect(url_for('index'))
            else:
                error = "Şifre yanlış."
                return render_template(
                            'login.html', error=error)
        else:
            error = "Kullanıcı bulunamadı."
            return render_template(
                            'login.html', error=error)                     
    else:
        return render_template('login.html')       