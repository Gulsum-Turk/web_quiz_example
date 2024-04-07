from flask import Flask, render_template, request, session, redirect, url_for, flash
from app import db, app
from app.models import User

#kayıt sayfası
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        name = request.form['name']

        # Kullanıcı adının daha önce kullanılıp kullanılmadığını kontrol et
        if User.query.filter_by(userName=username).first():
            error = 'Bu kullanıcı adı zaten kullanılıyor.'
            return render_template('register.html', error=error)

        # Parolaların eşleşip eşleşmediğini kontrol et
        if password != password2:
            error = 'Parolalar eşleşmiyor.'
            return render_template('register.html', error=error)

        # Parolanın en az 6 karakter uzunluğunda olduğunu kontrol et
        if len(password) < 6:
            error = 'Parola en az 6 karakter uzunluğunda olmalıdır.'
            return render_template('register.html', error=error)

        # Veritabanına kullanıcıyı ekle
        new_user = User(userName=username, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        message= "Kayıt Başarılı"
        
        flash(message, 'message')
        return redirect(url_for('login'))

    return render_template('register.html')


