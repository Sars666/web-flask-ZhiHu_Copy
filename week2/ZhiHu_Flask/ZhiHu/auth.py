import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from ZhiHu.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET','POST'))
def register():
    if request.method == 'POST':
    #如果用户提交了表单，那么 request.method 将会是 'POST'
        username = request.form['username']
        password = request.form['password']
        password_re = request.form['password_re']
        db = get_db()
        error = None

        if not username:
            error = '请输入用户名'
        elif not (password or password_re):
            error = '请输入密码'
        elif password != password_re:
            error = '两次输入密码不一致'
        elif db.execute(
            'SELECT userID FROM user WHERE username = ?',(username,)
        ).fetchone() is not None:
            error = '该用户名已被使用'

        if error is None:
            db.execute(
                'INSERT INTO user(username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',(username, )
        ).fetchone()

        if user is None:
            error = "账号或密码错误"
        elif not check_password_hash(user['password'],password):
            error = '账号或密码错误'

        if error is None:
            session.clear()
            session['userID'] = user['userID']
            return redirect(url_for('mainPage.asking'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    userID = session.get('userID')

    if userID is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE userID = ?',(userID,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('mainPage.asking'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.register'))

        return view(**kwargs)

    return wrapped_view