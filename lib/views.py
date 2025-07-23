from flask import render_template, request, redirect

from lib.config import *

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/users')
def admin_users():
    return render_template('admin/users.html')

@app.route('/admin/user/<int:user_id>')
def admin_user(user_id):
    return render_template('admin/user.html', user_id=user_id)

@app.route('/admin/admins')
def admin_admins():
    return render_template('admin/admins.html')

@app.route('/admin/answers')
def admin_answers():
    return render_template('admin/answers.html')

@app.route('/me')
def me():
    return render_template('me.html')
