from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from ZhiHu.auth import login_required
from ZhiHu.db import get_db
from ZhiHu.question import get_answers,get_questions,get_all_answers
from ZhiHu.user import get_user

bp = Blueprint('mainPage', __name__)

@bp.route('/',methods=('GET','POST'))
def asking():
    answers = get_all_answers()
    userID = session.get('userID')
    user = get_user(userID)

    if request.method == 'POST':
        ask_title = request.form['ask_title']
        ask_detail = request.form['ask_detail']
        db= get_db()
        error = None

        if not ask_title:
            error = '请输入问题'
        elif len(ask_title)>=33:
            error = '问题不能超过33个字'
        elif db.execute(
            'SELECT title FROM question WHERE title = ?',(ask_title,)
        ).fetchone() is not None:
            error = '已经存在该问题'

        if error is not None:
            flash(error)
        else:
            db.execute(
                'INSERT INTO question (title, detail)'
                ' VALUES (?, ?)',
                (ask_title, ask_detail)
            )
            ids=db.execute(
                'select questionID from question order by questionID desc;'
            ).fetchall()
            questionID= ids[0][0]
            db.commit()

            return redirect(url_for('question.add_answer',questionID = questionID))

    elif request.method == 'GET':
        return render_template('mainPage/frontPage.html', user=user,answers=answers)

def get_mainPageElements():
    questions = get_questions()
    answerList = []
    for i in range(len(questions)):
        question = questions[i]
        questionID = question[1]
        answers = get_answers(questionID)
        for answer in answers:
            answerList += answer #answers是一个二维元组  answer是一维元组

    mainPageElements =[]
    return mainPageElements

