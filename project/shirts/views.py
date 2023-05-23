from flask import Flask, url_for, render_template, Blueprint, request, flash
import flask_sqlalchemy
import flask_admin
import flask_security
from project import app
from project.models import Shirt


shirts_blueprint = Blueprint('shirts', __name__, template_folder='templates/shirts')
@shirts_blueprint.route('/shirts')
def shirts():
    shirts = Shirt.query.all()
    return render_template('shirts.html', shirts=shirts)