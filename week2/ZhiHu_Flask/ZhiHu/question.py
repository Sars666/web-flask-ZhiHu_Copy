from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from ZhiHu.auth import login_required
from ZhiHu.db import get_db

bp = Blueprint('question', __name__)

@bp.route('/question/<int:questionID>/',methods=('GET', 'POST'))
@login_required
def add_answer(questionID):
    question = get_question(questionID)
    answers = get_answers(questionID)

    if request.method == 'POST':
        userID = session.get('userID')
        answer = request.form['answer']
        error = None

        if answer == '' or (answers is None):
            error = '请输入回答'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO answer(userID, questionID, answer) VALUES (?, ?, ?)',
                (userID, questionID, answer)
            )
            db.commit()

        return redirect(url_for('question.add_answer',questionID=questionID))

    elif request.method =='GET':
        return render_template('mainPage/question.html',question=question,answers=answers)

def get_questions():
    questions = get_db().execute(
        'SELECT questionID,title'
        ' FROM question'
        ' ORDER BY created DESC ',
        ).fetchall()
    return questions

def get_question(questionID):
    question = get_db().execute(
        'SELECT questionID, title, detail, created '
        ' FROM question'
        ' WHERE questionID = ?',
        (questionID,)
    ).fetchone()
    return question

def get_answers(questionID):
    answers = get_db().execute(
        'SELECT a.questionID,answer, a.created, upvote'
        ' FROM answer a'
        ' JOIN question q ON a.questionID = q.questionID'
        ' WHERE a.questionID = ?'
        ' ORDER BY a.created DESC ',
        (questionID,)
    ).fetchall()
    return answers

'''
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_question(id)

    if request.method == 'POST':
        title = request.form['title']
        detail = request.form['detail']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, content = ?'
                ' WHERE id = ?',
                (title, detail, id)
            )
            db.commit()
            return redirect(url_for('mainPage.frontPage'))

    return render_template('mainPage/front_update.html', post=post)
'''

'''
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_question(id)
    db = get_db()
    db.execute('DELETE FROM question WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('mainPage.frontPage'))

'''