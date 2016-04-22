
from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, abort, request, session, g
from flask.ext.login import login_user, \
    login_required, logout_user  
from .forms import LoginForm, RegisterForm
from project import db  
from project.models import User, bcrypt  
from uuid import uuid4
from werkzeug.routing import NotFound

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   
_exempt_views = []

def csrf_exempt(view):
    _exempt_views.append(view)
    return view


def csrf(app, on_csrf=None):
    @app.before_request
    def _csrf_check_exemptions():
        try:
            dest = app.view_functions.get(request.endpoint)
            g._csrf_exempt = dest in _exempt_views
        except NotFound:
            g._csrf_exempt = False
    
    @app.before_request
    def _csrf_protect():
        # This simplifies unit testing, wherein CSRF seems to break
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

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')  
@login_required  
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST']) 
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)