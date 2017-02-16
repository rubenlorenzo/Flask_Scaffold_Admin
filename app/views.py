from flask import render_template
from flask import request, url_for, redirect, flash
from flask_user import login_required, confirm_email_required, roles_required, current_user
from app import app, db
from app.models import User, Role, UserRoles
from sqlalchemy.orm import aliased
from sqlalchemy.exc import IntegrityError
from forms import UserForm, RoleForm
from array import array
from sqlalchemy.sql import exists


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
@app.route('/members/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', user=db.session.query(User).filter(User.username == username).first())


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
    return render_template('edit_profile.html',
                           form=form, name=request.args.get('name'))


#Admin_page - route
@app.route('/admin/page')
@roles_required('admin')
def admin_page():
    return render_template('admin_page.html')


#Edit_profile_roles - route
@app.route('/members/profile/roles/edit/<username>' ,methods=['GET','POST'])
@roles_required('admin')
def  edit_profile_roles(username):
    user=db.session.query(User).filter(User.username == username).first()

    form_user = UserForm()
    form_role = RoleForm()

    return render_template(
        'edit_profile_roles.html',
         user=user,
          form_user=form_user, form_role=form_role,roles=db.session.query(Role).all())


#Add_role - route
@app.route('/members/roles/add' ,methods=['GET','POST'])
@roles_required('admin')
def add_role():
    form_role = RoleForm()

    # Process valid POST
    if request.method == 'POST' and form_role.validate():
        #Add role, if role not exist
        if not Role.query.filter(Role.name==form_role.name.data).first():
            role = Role(name=form_role.name.data)
            db.session.add(role)
            db.session.commit()
        else:
            flash(('Role '+form_role.name.data+' exist.'), 'success')

        return redirect(url_for('edit_profile_roles', username=request.args.get('user')))

    return redirect(url_for('edit_profile_roles', username=request.args.get('user')))

#Add_role - route
@app.route('/members/roles/add/<username>' ,methods=['GET','POST'])
@roles_required('admin')
def add_role_user(username) :
    user=db.session.query(User).filter(User.username == username).first()
    form_role = RoleForm()

    if request.method == 'POST' and form_role.validate() :
        remove_roles= [ ]

        for r_user in user.roles :
            role_status=False

            for r_name in request.form.getlist("name") :
                if r_user.name == r_name :
                    role_status=True

            if not role_status :
                remove_roles.append(r_user.name)

        for r_role in remove_roles :        
            role=db.session.query(Role).filter(Role.name==r_role).first()
            user.roles.remove(role)
            db.session.commit()

        for r_name in request.form.getlist("name") :
            role=db.session.query(Role).filter(Role.name==r_name).first()

            if not db.session.query(User).join(User.roles).filter(User.username==user.username, Role.name==role.name).first() :
                user.roles.append(role)
                db.session.commit()

    return redirect(url_for('edit_profile_roles', username=username))
