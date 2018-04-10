from flask import render_template
from app import app


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
