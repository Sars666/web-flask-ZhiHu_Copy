import os
from flask import Flask
from flask_script import Manager

def create_app(test_config=None):
    # 创建app 设置配置
    app = Flask(__name__, instance_relative_config=True)
    app.config['DEBUG'] = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ZhiHu.sqlite'),
    )
    if test_config is None:
        # 非测试模式加载配置
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 加载测试配置
        app.config.from_mapping(test_config)

    # 保证实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import mainPage
    app.register_blueprint(mainPage.bp)
    app.add_url_rule('/', endpoint='index')

    from . import question
    app.register_blueprint(question.bp)

    from . import user
    app.register_blueprint(user.bp)

    return app

