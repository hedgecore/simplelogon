from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, abort, request, session, g
from flask.ext.login import login_user, \
    login_required, logout_user  
from .forms import LoginForm, RegisterForm
from project import db  
from project.models import User, bcrypt  

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   
<<<<<<< HEAD
=======
_exempt_views = []

def csrf_exempt(view):
    _exempt_views.append(view)
    return view

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid4())
    return session['_csrf_token']
    
app.jinja_env.globals['csrf_token'] = generate_csrf_token
>>>>>>> 415c4d83f8fe78b9cb7548bcc76822da518b856d

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
                flash('You are logged in.')
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
