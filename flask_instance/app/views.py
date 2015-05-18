from flask import render_template, redirect, url_for, flash, g, request
from app import app
from app.forms import LoginForm
from app import lm, oid, db
from app.models import User
from flask.ext.login import login_user, logout_user, current_user, login_required


@app.route('/')
def root():
    return render_template("root.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    users = {'nickname': "acezio"}
    posts = [
        {'author': {'nickname': "John"},
         'body': "Hello JinJia2"},
        {'author': {'nickname': "Boss"},
         'body': "Tomorrow give me your paper"}
    ]
    return render_template("index.html", title="acezio", users=users, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for(index))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',
                           form=form, title='title', providers=app.config['OPENID_PROVIDERS'])


@lm._load_user(id)
def load_user(id):
    return User.query.get(int(id()))