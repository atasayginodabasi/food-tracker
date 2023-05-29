from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from foodTracker import db
from foodTracker.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from foodTracker.models import User
from foodTracker.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


# Register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    fullname=form.fullname.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)

            flash("Log in Success!")

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('home_page.home')

            return redirect(next)
    return render_template('login.html', form=form)


# Logout User
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home_page.home"))


# Account (update UserForm)
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.fullname = form.fullname.data

        db.session.commit()

        flash('User Account Updated!')

        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.fullname.data = current_user.fullname

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)

    user = User.query.filter_by(id=current_user.id).first_or_404()

    return render_template('account.html',
                           profile_image=profile_image,
                           form=form,
                           user=user)
