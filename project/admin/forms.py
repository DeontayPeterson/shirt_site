from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, FileField, TextAreaField
from wtforms.validators import DataRequired

# Login form for admin. Could update to later include other users. 
class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Login")

class AddForm(FlaskForm):
    name = StringField("Shirt Name: ", validators=[DataRequired()])
    price = FloatField("Shirt Price: ", validators=[DataRequired()])
    description = TextAreaField("Shirt Description")
    thumbnail = FileField("Image of Shirt")
    submit = SubmitField("Add shirt")

class RemoveForm(FlaskForm):
    to_remove = StringField('Shirt name to remove: ')
    submit = SubmitField("Remove")


    