from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ZhiHu.auth import login_required
from ZhiHu.db import get_db
from ZhiHu.question import get_answers,get_questions,get_all_answers

bp = Blueprint('mainPage', __name__)

@bp.route('/',methods=('GET','POST'))
def asking():
    answers = get_all_answers()

    if request.method == 'POST':
        ask_title = request.form['ask_title']
        ask_detail = request.form['ask_detail']
        error = None

        if not ask_title:
            error = '请输入问题'
        elif len(ask_title)>=33:
            error = '问题不能超过33个字'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO question (title, detail)'
                ' VALUES (?, ?)',
                (ask_title, ask_detail)
            )
            db.commit()

            questionID = db.execute(
                'SELECT title'
                ' FROM question'
                ' WHERE title = ?',
                    (ask_title,)
            )
            return redirect(url_for('mainPage.question',questionID = questionID[0]))

    elif request.method == 'GET':
        return render_template('mainPage/frontPage.html', answers=answers)

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

