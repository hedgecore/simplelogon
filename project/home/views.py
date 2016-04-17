from project import db, app, hm
from project.models import BlogPost
from forms import MessageForm
#from flask_hmac import Hmac 
from flask import render_template, Blueprint, flash, url_for, redirect, request
from flask.ext.login import login_required,  current_user
#from flask_wtf.csrf import CsrfProtect


#### config ####

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

	
#### routes ####


# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.name.data,
            form.email.data
            # current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('Your information is updated. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
