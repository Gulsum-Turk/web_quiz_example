from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import User


@app.route('/logout', methods=["get","post"])
def logout():
    session.clear()
    return redirect(url_for('index'))