from flask import Flask, url_for, render_template, Blueprint, request, flash
from project.contact.forms import ContactForm
import flask_sqlalchemy
import flask_admin
import flask_security
from flask_mail import Mail, Message
from project import app

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'africanmangoenjoyer@gmail.com'
app.config['MAIL_PASSWORD']  = ''

mail = Mail(app)


contact_blueprint = Blueprint('contact', __name__, template_folder='templates/contact')

@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone_number.data
        email = form.email.data
        message = form.message.data
        send_message(name=name, email=email, body=message)

    return render_template('contact.html', form=form)

def send_message(name, email, body):
    msg = Message(subject='New Message From Website',
                  sender=("Contact form", email),
                  recipients=['africanmangoenjoyer@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {body}"
    mail.send(msg)

    flash('Message sent!')
    
