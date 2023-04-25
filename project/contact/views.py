from flask import Flask, url_for, render_template, Blueprint
from project.contact.forms import ContactForm
import flask_sqlalchemy
import flask_admin
import flask_security

contact_blueprint = Blueprint('contact', __name__, template_folder='templates/contact')

@contact_blueprint.route('/contact', methods=['GET'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone_number.data
        email = form.email.data
        message = form.message.data

    return render_template('contact.html', form=form)

