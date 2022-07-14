from flask import (
    Blueprint,
    render_template, 
    g,
    request,
    session,
    redirect,
    url_for
)
from app import app
from app.forms import user as user_forms
import json
from json import dumps

# Create a user blueprint
userbp = Blueprint('userbp', __name__, url_prefix='/user')


@userbp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = user_forms.SignUp()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('index'))

    return render_template('user/signup.html', form=form, title='Sign Up')


@userbp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = user_forms.SignIn()
    return render_template('user/signin.html', form=form, title='Sign In')
