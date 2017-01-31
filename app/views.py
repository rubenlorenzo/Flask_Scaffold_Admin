from flask import render_template
from flask_user import login_required, roles_required
from app import app, db
from app.models import User, Role

#Root - route
@app.route('/')
def home_page():
    return render_template('index.html')

#Members - route
@app.route('/members')
@login_required
def members_page():
    return render_template('members.html', users=db.session.query(User).all())

#Admin_page - route
@app.route('/admin/page')
@roles_required('admin')
def admin_page():
    return render_template('admin_page.html',)
