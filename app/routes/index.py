# routes/index.py
from flask import render_template,session
from app import app
from app.models import LeaderTable
from sqlalchemy import desc



@app.route('/')
def index():
    top_three_users = LeaderTable.query.order_by(desc(LeaderTable.puan)).limit(3).all()
    logged_in = False
    username = None
    if 'username' in session:
        logged_in = True
        username = session['username']

# Kullanıcı adlarını ve puanlarını al
    
    return render_template('index.html', logged_in=logged_in, username=username, users= top_three_users)

