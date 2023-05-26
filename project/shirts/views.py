from flask import Flask, url_for, render_template, Blueprint, request, flash
import flask_sqlalchemy
import flask_admin
import flask_security
from project import app
from project.models import Shirt
from .forms import OrderForm


shirts_blueprint = Blueprint('shirts', __name__, template_folder='templates/shirts')

@shirts_blueprint.route('/shirts')
def shirts():
    shirts = Shirt.query.all()
    return render_template('shirts.html', shirts=shirts)


@shirts_blueprint.route('/shirt_detail/<int:shirt_id>')
def shirt_detail(shirt_id):
    order_form = OrderForm()
    shirt = Shirt.query.get_or_404(shirt_id)
    return render_template('shirt_detail.html', shirt=shirt, order_form = order_form)
