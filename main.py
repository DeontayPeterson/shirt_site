from flask import Flask, url_for, render_template
from forms import ContactForm
import flask_sqlalchemy
import flask_admin
import flask_security


app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/')
def landing_page():

    return render_template('landing.html')


@app.route('/home')
def index():

    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        phone_number = form.phone_number.data
        email = form.email.data
        message = form.message.data


    return render_template('contact.html', form=form)

@app.route('/test')
def test():
    return render_template('test.html')



app.run(debug=True)
