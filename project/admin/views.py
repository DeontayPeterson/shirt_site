from flask import redirect, url_for, render_template, flash, request, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from project.user import User
from .forms import LoginForm, AddForm, RemoveForm
from project.models import Shirt
from project import db 

admin_blueprint = Blueprint('admin', __name__, template_folder='templates/admin')

# Login route for admin dashboard.
@admin_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.is_admin and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid Username or Password', 'danger')
    return render_template('login.html', form=form)



@admin_blueprint.route('/logout',)
@login_required
def logout():

    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))


# Route for admin dashboard
@admin_blueprint.route('/dashboard',methods=['GET']) 
@login_required
def dashboard():  

    addform = AddForm()
    removeform = RemoveForm()
    if not current_user.is_admin:
        flash("You don't have permission to view this page.", 'danger')
        return redirect(url_for('main.idex'))
    
    return render_template('dashboard.html', forms={'addform': addform, 'removeform': removeform})


@admin_blueprint.route('/dashboard/add_shirt', methods=['POST'])
@login_required
def add_shirt():

    addform = AddForm()
    #TODO Add error handling. 
    if request.method == "POST":
        shirt = Shirt(name=addform.name.data, price=addform.price.data, description=addform.description.data,
                        thumbnail=addform.thumbnail.data, )
        db.session.add(shirt)
        db.session.commit()
        flash('Shirt has been added to the database')
    
    return redirect(url_for('admin.dashboard'))


@admin_blueprint.route('/dashboard/view') 
@login_required
def view():
    return render_template('view.html')


