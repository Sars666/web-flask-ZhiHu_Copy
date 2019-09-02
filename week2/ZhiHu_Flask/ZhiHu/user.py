from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ZhiHu.auth import login_required
from ZhiHu.db import get_db

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['GET','POST'])
@login_required
def show_user():
    userID=session.get('userID')
    user = get_user(userID)
    return render_template('mainPage/user.html' ,user=user)

def get_user(userID):
    user = get_db().execute(
        'SELECT userID, nickname, sign, headurl '
        ' FROM user'
        ' WHERE userID = ?',
        (userID,)
    ).fetchone()
    return user

@bp.route('/user/edit', methods=['POST','GET'])
def edit_user():
    userID=session.get('userID')
    user = get_user(userID)

    if request.method == 'POST':
        userID = session.get('userID')
        nickname = request.form['nickname']
        sign = request.form['sign']
        headurl = request.form['headurl']

        error = None

        if nickname == '' or (nickname is None):
            error = '昵称不能为空'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE user'
                ' SET (nickname,sign,headurl)'
                ' (?, ?, ?)',
                (nickname, sign, headurl)
            )
            db.commit()
        return redirect(url_for('user.show_user',userID=userID))

    elif request.method =='GET':
        return render_template('mainPage/user_edit.html',user=user)