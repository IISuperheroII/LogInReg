from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

class UserInfo(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmPassword = PasswordField("Password (Confirm)", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.email = user_data['email']
        self.password = user_data['password']

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
class Note():
    data = TextAreaField("data", validators= [DataRequired()])



