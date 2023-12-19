from application import app
from flask import request, redirect, render_template, url_for, flash

from .forms import UserInfo
from datetime import datetime
from application import db


from application import app
from flask import request, redirect, render_template, flash
from .forms import UserInfo
from datetime import datetime
from application import db

@app.route("/", methods=['POST', 'GET'])
def index():
    form = UserInfo()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        db.user_data.insert_one({
            "username": username,
            "email": email,
            "password": password,
            "date_created": datetime.utcnow()
        })

        flash("Signed up successfully", "success")
        return redirect("/")

    return render_template("SignUp.html", title="Sign Up", form=form)