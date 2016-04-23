from project import db, app
from project.models import information
from forms import MessageForm

from flask import render_template, Blueprint, flash, url_for, redirect, request, abort, request, session, g
from flask.ext.login import login_required,  current_user
import sqlalchemy 
from uuid import uuid4
from werkzeug.routing import NotFound


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)
_exempt_views = []

def csrf(app, on_csrf=None):
    @app.before_request
    def _csrf_protect():
        if app.config.get('TESTING'):
            return
        if not g._csrf_exempt:
            if request.method == "POST":
                csrf_token = session.pop('_csrf_token', None)
                if not csrf_token or csrf_token != request.form.get('_csrf_token'):
                    if on_csrf:
                        on_csrf(*app.match_request())
                    abort(400)
    
    def generate_csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = str(uuid4())
        return session['_csrf_token']
    
    app.jinja_env.globals['csrf_token'] = generate_csrf_token

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
