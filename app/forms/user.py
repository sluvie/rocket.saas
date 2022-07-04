from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)

class Login(Form):
    email = TextField(validators=[Required(), Email()], description="Email address")
    