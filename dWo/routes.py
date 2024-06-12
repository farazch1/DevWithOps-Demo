from flask_login import login_user, logout_user, current_user
from dWo import app, db
from flask import render_template, redirect, url_for, flash
from dWo.models import User
from dWo.forms import FormSignUp, LoginForm
import time


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    return render_template('index4.html')

@app.route('/after_login')
def after_login():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def sign_up():
    form = FormSignUp()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_add=form.email_address.data,
                              password= form.password1.data
                              )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('signupForm.html', form = form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            return redirect(url_for('after_login'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('LoginForm.html', form=form)

@app.route('/logout')
def log_out():
    logout_user()
    return redirect(url_for("hello_world"))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/compete')
def compete():
    return render_template('compete.html')

@app.route('/others')
def other():
    return render_template('others.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/mylearning')
def my_learning():
    return render_template('mylearning.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/cloudlabs')
def cloudlabs():
    return render_template('clabs.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/personal_paths')
def p_paths():
    return render_template('perpaths.html')

@app.route('/skills_path')
def s_paths():
    return render_template('skillspaths.html')

@app.route('/assessment')
def assessment():
    return render_template('assess.html')

@app.route('/azure_track')
def Azure():
    return render_template('azure.html')

@app.route('/linux_track')
def Linux():
    return render_template('linux.html')

@app.route('/e2c_track')
def EC2():
    return render_template('ec2.html')

