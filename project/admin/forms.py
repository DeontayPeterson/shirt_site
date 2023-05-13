from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, FileField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

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
    to_remove = StringField('Shirt Name to Remove: ')
    submit = SubmitField("Remove")

class EditShirt(FlaskForm):
    name = StringField('New Name For Shirt: ', validators=[InputRequired()])
    price = FloatField("Enter New Price for Shirt: ", validators=[InputRequired()])
    description = TextAreaField("Enter New Description for Shirt: ")
    submit = SubmitField('Update Shirt')



    