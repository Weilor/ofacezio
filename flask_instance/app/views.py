from app import app
from flask import render_template

@app.route('/')
def root():
    return render_template("root.html")


@app.route('/index')
def index():
    users = {'nickname': "acezio"}
    posts = [
        {'author': {'nickname': "John"},
         'body': "Hello JinJia2"},
        {'author': {'nickname': "Boss"},
         'body': "Tomorrow give me your paper"}
    ]
    return render_template("index.html", title="acezio", users=users, posts=posts)
