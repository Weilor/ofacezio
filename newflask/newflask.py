import os
from flask import Flask, request, make_response, redirect, abort, render_template, session, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "website of acezio"
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class NameForm(Form):
    name = StringField("你的名字是什么？", validators=[Required()])
    submit = SubmitField("提交")


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return "Username is %s" % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "Rolesname is %s" % self.name

@app.route('/hello')
def hello_world():
    return """<h1>Hello World!你好世界！</h1>
    %s
    """ % request.headers.get('User-Agent')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("欢迎回来 %s" % form.name.data)
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("login"))
    return render_template("form.html", name=session.get("name"), form=form)


@app.route("/index")
def index():
    return render_template("index.html", name="han")


@app.route("/twitter/<username>")
def twitter(username):
    return render_template("user.html", name=username)


@app.route('/user/<username>')
def user(username):
    response = make_response("hello,%s" % username)
    response.set_cookie('answer', '11')
    return response


@app.route("/baidu")
def baidu():
    return redirect("http://www.baidu.com")


@app.route('/400')
def not_find():
    abort(404)
    return "你来到了服务器的荒野"


@app.route('/number/<post_id>', methods=['GET', 'POST'])
def number(post_id):
    if request.method == 'GET':
        return "It's %d" % post_id
    else:
        return "bye"


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
