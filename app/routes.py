from flask import render_template, flash, redirect, url_for
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Uzul"}
    posts = [
        {
            'author': {'username': 'user1'},
            'body': 'text 1'
        }
    ]
    return render_template('index.html', title="hhome", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        txt = 'Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data)
        flash(txt)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)