from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=20)])
    username = StringField("Username", [validators.Length(min=4, max=14)])
    password = PasswordField("Password", [validators.Length(min=4, max=14)])
    role = SelectField("Role", choices=[('USER', 'User'), ('ADMIN', 'Admin')])

    class Meta:
        csrf = False