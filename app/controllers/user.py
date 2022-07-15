from flask import (
    Blueprint,
    render_template, 
    g,
    request,
    session,
    redirect,
    url_for,
    flash
)
import flask_login

from app import app
from app.forms import user as user_forms
import json
from json import dumps

from app.libraries.session import usersession as USession

# Create a user blueprint
userbp = Blueprint('userbp', __name__, url_prefix='/user')


@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = user_forms.SignUp(request.form)

    # form submit
    if request.method == 'POST' and form.validate():
        return redirect(url_for('index'))

    return render_template('user/signup.html', form=form, title='Sign Up')


@userbp.route('/signin', methods=['GET', 'POST'])
def signin():
    # if already login, redirect to home
    if 'usersession' in session and session["usersession"] is not None:
        return redirect(url_for('home'))

    form = user_forms.SignIn(request.form)

    # initialize sample input
    if request.method=="GET":
        form.email.data = "demo@rocket.com"

    # form submit
    if request.method=="POST" and form.validate():
        if form.email.data == "demo@rocket.com" and form.password.data == "demodemo":
            # process the login manager session
            user = USession.User()
            # TODO: place your user / account data
            user.name = form.email.data
            user.email = form.email.data

            # save to session
            session["usersession"] = user.__dict__
            flask_login.login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid account.', 'negative')
            return redirect(url_for('userbp.signin'))

    return render_template('user/signin.html', form=form, title='Sign In')


@userbp.route('/signout')
@flask_login.login_required
def signout():
    flask_login.logout_user()
    session["usersession"] = None
    flash('Succesfully signed out.', 'positive')
    return redirect(url_for('index'))


@userbp.route('/profile')
@flask_login.login_required
def profile():
    return render_template('user/profile.html', title='Profile')


@userbp.route('/browse')
@flask_login.login_required
def browse():
    return render_template('user/browse.html', title='Users')