from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

# form for creating a new account
class RegisterForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# form for logging in to an account
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# form to change password
class ChangeForm(Form):
    old = PasswordField('Old', validators=[DataRequired()])
    new = PasswordField('New', validators=[DataRequired()])
