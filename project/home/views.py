from project import db, app
from project.models import information
from forms import MessageForm

from flask import render_template, Blueprint, flash, url_for, redirect, request
from flask.ext.login import login_required,  current_user
import sqlalchemy 

#### config ####

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

	
#### routes ####


#  decorators 
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required  
def home():
    error = None
    form = MessageForm(request.form)
    #db.session.delete(information)
    if form.validate_on_submit():
        new_message = information(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('Your information was successfully updated. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(information).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')  
def welcome():
    return render_template('welcome.html') 