from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from flask import request, redirect, render_template, flash, url_for
from .forms import UserInfo, Note, User
from datetime import datetime
from application import db

@app.route("/", methods=['POST', 'GET'])
def signup():
    form = UserInfo()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password= form.password.data
        confirmPassword= form.confirmPassword.data

        user = db.user_data.find_one({'email': email})

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != confirmPassword:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            hashed_password = password
            new_user = {
                'email': email,
                'first_name': username,
                'password': hashed_password,
                'date_created': datetime.utcnow()
            }
            db.user_data.insert_one(new_user)
            flash('Account created!', category='success')
            return redirect(url_for('login'))
    return render_template("signUp.html", title="Sign Up", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserInfo()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user_data = db.user_data.find_one({'email': email})

        if user_data and user_data['password'] == password:
            user = User(user_data)
            login_user(user, remember=True)
            flash('Logged in successfully!', category='success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password, try again.', category='error')

    return render_template("logIn.html", user=current_user, form=form)
@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_data = Note.data.data  # Assuming your HTML form has an input field with name 'note'

        if len(note_data) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = {
                'note': note_data,
                'date_created': datetime.utcnow(),
                'id_user_created': current_user._id
            }
            db.user_data.insert_one(new_note)

            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)