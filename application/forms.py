from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class UserInfo(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    email = EmailField("E-mail", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    submit = SubmitField("Sign Up")

