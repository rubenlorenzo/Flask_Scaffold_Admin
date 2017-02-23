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
    return render_template('index.html', title="Home")


#Members - route
@app.route('/members')
@login_required
def members_page():
    return render_template('members.html', users=db.session.query(User).all(),
        title="Members")


#Users_profile - route
@app.route('/members/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html',
        user=db.session.query(User).filter(User.username == username).first(),
         title="Members", subtitle="Profile")


#CurrentUser_profile_edit - route
@app.route('/members/myprofile/edit', methods=['GET', 'POST'])
@login_required
def edit_myprofile():
    # Initialize form
    form_user = UserForm()

    # Process valid POST
    if request.method == 'POST' and form_user.validate():
        # Copy form fields to user_profile fields
        form_user.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('edit_myprofile'))

    # Process GET or invalid POST
    return render_template('edit_myprofile.html',
        form_user=form_user, name=request.args.get('name'), title="Members",
        subtitle="Edit profile")

#CurrentUser_admin_role_profile_edit - route
@app.route('/members/myprofile/edit/admin', methods=['GET', 'POST'])
@roles_required('admin')
def edit_myprofile_roles():
    # Initialize form
    form_user = UserForm()
    form_role = RoleForm()

    # Process valid POST
    if request.method == 'POST' and form_user.validate():
        # Copy form fields to user_profile fields
        form_user.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('edit_myprofile_roles'))

    return render_template('edit_myprofile_roles.html', form_user=form_user,
        form_role=form_role, roles=db.session.query(Role).all(),
        name=request.args.get('name'), title="Members", subtitle="Profile edit")

#Admin_page - route
@app.route('/admin/page')
@roles_required('admin')
def admin_page():
    return render_template('admin_page.html', title="Admin")


#Edit_profile_roles - route
@app.route('/members/profile/roles/edit/<username>' ,methods=['GET','POST'])
@roles_required('admin')
def  edit_profile_roles(username):
    user=db.session.query(User).filter(User.username == username).first()

    # Initialize form
    form_user = UserForm()
    form_role = RoleForm()

    return render_template('edit_profile_roles.html', user=user, form_user=form_user,
        form_role=form_role,roles=db.session.query(Role).all(), title="Members",
        subtitle="Profile edit")

#Roles - route
@app.route('/roles')
@roles_required('admin')
def roles_page():
    form_role = RoleForm()

    return render_template('roles.html', form_role=form_role, roles=db.session.query(Role).all(), title="Roles")

#Add_role - route
@roles_required('admin')
@app.route('/roles/add' ,methods=['GET','POST'])
def add_role():
    # Initialize form
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

    return "None"


#Add_role to user - route
@app.route('/members/roles/add/<username>' ,methods=['GET','POST'])
@roles_required('admin')
def add_role_user(username) :
    user=db.session.query(User).filter(User.username == username).first()

    #User is current_user
    user_is_current_user=False
    if user == current_user:
        user_is_current_user=True

    form_role = RoleForm()

    if request.method == 'POST' and form_role.validate() :
        #Remove deselect roles
        remove_roles= [ ]

        #User Roles
        role_admin=False
        for r_user in user.roles :
            role_status=False

            #Role admin user
            if r_user.name == "admin" :
                role_admin=True

            #Roles checks
            for r_name in request.form.getlist("name") :
                #Compare with roles user, true If the role remains checked
                if r_user.name == r_name :
                    role_status=True
            #Add array remove_roles, If the role does not remains checked
            if not role_status :
                remove_roles.append(r_user.name)


        #Removes roles that are not checked now
        for r_role in remove_roles :
            role=db.session.query(Role).filter(Role.name==r_role).first()
            user.roles.remove(role)
            db.session.commit()

        #Add roles checked
        for r_name in request.form.getlist("name") :
            role=db.session.query(Role).filter(Role.name==r_name).first()

            #If it does not belong to the user it adds it
            if not db.session.query(User).join(User.roles).filter(User.username==user.username, Role.name==role.name).first() :
                user.roles.append(role)
                db.session.commit()

    if user_is_current_user and role_admin :
        return redirect(url_for('edit_myprofile_roles', username=username))
    else:
        return redirect(url_for('edit_profile_roles', username=username))

#Remove_role - route
@app.route('/roles/remove', methods=['POST'])
@roles_required('admin')
def remove_role():

    if request.method == 'POST' :
        role_remove=db.session.query(Role).filter(Role.name==request.form["role_remove"]).first()

        db.session.delete(role_remove)
        db.session.commit()

    return "None"
