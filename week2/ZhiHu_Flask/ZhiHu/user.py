from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ZhiHu.auth import login_required
from ZhiHu.db import get_db
import os
from werkzeug.utils import secure_filename
import uuid
bp = Blueprint('user', __name__)


@bp.route('/user', methods=['GET', 'POST'])
@login_required
def show_user():
    userID = session.get('userID')
    user = get_user(userID)
    return render_template('mainPage/user.html', user=user)


def get_user(userID):
    user = get_db().execute(
            'SELECT userID, nickname, sign, headurl '
            ' FROM user'
            ' WHERE userID = ?',
            (userID,)
    ).fetchone()
    return user


@bp.route('/user/edit', methods=['POST', 'GET'])
def edit_user():
    userID = session.get('userID')
    user = get_user(userID)

    if request.method == 'POST':
        userID = session.get('userID')
        nickname = request_form(user,'nickname')
        if request.files.get('headImg') is not None:
            headImg = request.files['headImg']
            uuid_str = uuid.uuid4().hex
            img_name = uuid_str + '.jpg'
            basepath = os.path.dirname(__file__)
            headurl = os.path.join('/static/img/uploads',
                                   secure_filename(img_name))
            headImg.save(os.path.join(basepath,'static/img/uploads',
                                   secure_filename(img_name)))
        else:
            headurl = user['headurl']

        sign = request_form(user,'sign')
        db = get_db()
        db.execute(
                'UPDATE user SET nickname = ? , sign = ?, headurl= ?'
                ' WHERE userID = ?',
                (nickname, sign, headurl, userID)
        )
        db.commit()
        return redirect(url_for('user.edit_user'))

    elif request.method == 'GET':
        return render_template('mainPage/user_edit.html', user=user)


def request_form(table,para):
    if request.form.get(para) is not None:
        var = request.form.get(para)
    else: var =table[para]

    return var