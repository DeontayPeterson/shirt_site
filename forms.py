from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, TextAreaField, SubmitField

# Form to contact owner.
class ContactForm(FlaskForm):
    name = StringField("Name: ")
    phone_number = StringField("Phone Number: ")
    email = StringField("Email Address: ")
    message = TextAreaField("Message: ")
    submit = SubmitField('Send Message!')



