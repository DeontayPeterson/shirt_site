from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, FileField, TextAreaField, SelectField
from wtforms_components import ColorField
from wtforms.validators import DataRequired, InputRequired


class OrderForm(FlaskForm):
    shirt_size = SelectField(choices=['XL', " L", "M", "S"])
    shirt_color = StringField()


    shirt_style = SelectField(choices=['T-shirt', 'V-neck'])
    shirt_fit = SelectField(choices=['Male', 'Female'])
    submit = SubmitField('ADD TO CART')


    # shirt_color = ColorField('Color') <-- Allows the user to select too many colors.

    

