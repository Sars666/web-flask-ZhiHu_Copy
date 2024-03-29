import sqlite3

import click,os
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import check_password_hash, generate_password_hash



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    #清理旧表,建立新表用以存储数据
    init_db()
    basepath = os.path.dirname(__file__)
    path = os.path.join(basepath,'static/img/uploads/')
    for img in os.listdir(path):
        img_path = os.path.join(path,img)
        os.remove(img_path)
    click.echo('数据库初始完成')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def init_test():
    db=get_db()
    db.execute(
        'INSERT INTO user(username,password,nickname,sign)'
        'VALUES (?,?,?,?)',
            ('test',generate_password_hash('test'),'测试用户','测试签名')
    )
    db.execute(
        'INSERT INTO question(title,detail)'
        'VALUES (?,?)',
            ('测试问题','测试问题详情')
    )
    db.execute(
        'INSERT INTO answer(answer,questionID,answerID)'
        'VALUES (?,?,?)',
            ('测试答案',1,1)
    )