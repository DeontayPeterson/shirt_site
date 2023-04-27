from flask import Flask, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user
import flask_sqlalchemy
import flask_admin
import flask_security
from project import app


@app.route('/')
def index():
    if current_user.is_authenticated:
        is_authenticated = True
    else:
        is_authenticated = False

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)