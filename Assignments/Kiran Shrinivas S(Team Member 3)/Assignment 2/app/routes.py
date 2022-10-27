from flask import render_template, url_for, redirect
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data = {}
        user_data['username'] = form.username.data
        user_data['email'] = form.email.data
        user_data['roll_no'] = form.roll_no.data
        user = User(**user_data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        return redirect(url_for('welcome', user_id=user.id))
    return render_template('login.html', form=form)


@app.route('/welcome/<user_id>', methods=['GET'])
def welcome(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('welcome.html', user=user)