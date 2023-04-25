from flask import Flask, url_for, render_template
import flask_sqlalchemy
import flask_admin
import flask_security
from project import app


@app.route('/')
def index():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)