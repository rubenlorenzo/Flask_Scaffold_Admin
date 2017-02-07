from flask import render_template
from flask import request, url_for, redirect
from flask_user import login_required, confirm_email_required, roles_required, current_user
from app import app, db
from app.models import User, Role
from sqlalchemy.orm import aliased
from forms import UserForm


#Root - route
@app.route('/')
def home_page():
    return render_template('index.html')

#Members - route
@app.route('/members')
@login_required
def members_page():
    return render_template('members.html', users=db.session.query(User).all())

#Users_profile - route
@app.route('/members/profile/<name>')
@login_required
def profile(name):
    return render_template('profile.html', user=db.session.query(User).filter(User.username == name).first())

#User_profile_edit - route
@app.route('/members/myprofile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    # Initialize form
    form = UserForm()

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('edit_profile'))

    # Process GET or invalid POST
    print  request.args.get('name')
    return render_template('edit_profile.html',
                           form=form, name=request.args.get('name'))


#Admin_page - route
@app.route('/admin/page')
@roles_required('admin')
def admin_page():
    return render_template('admin_page.html')
