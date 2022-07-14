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
from app import app
from app.forms import user as user_forms
import json
from json import dumps

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
    form = user_forms.SignIn(request.form)

    # initialize sample input
    if request.method=="GET":
        form.email.data = "demo@rocket.com"

    # form submit
    if request.method=="POST" and form.validate():
        if form.email.data == "demo@rocket.com" and form.email.data == "demodemo":
            return redirect(url_for('index'))
        else:
            flash('Invalid account.', 'negative')
            return redirect(url_for('userbp.signin'))

    return render_template('user/signin.html', form=form, title='Sign In')
