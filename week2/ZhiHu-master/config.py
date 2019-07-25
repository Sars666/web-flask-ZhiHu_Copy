#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#基类 Config 中包含通用配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '3225601523@qq.com'
    MAIL_PASSWORD = 'mthuzxexozdmcgih'
    FLASKY_MAIL_SUBJECT_PREFIX = 'zhihu'
    FLASKY_MAIL_SENDER = '3225601523@qq.com'
    FLASKY_ADMIN = '584807419@qq.com'
    FLASKY_POSTS_PER_PAGE = 10
    FLASK_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_ANSWERS_PER_PAGE = 30

    WHOOSH_BASE = os.path.join(basedir, 'WHOOSH_BASE_INDEX')

    CACHE_TYPE = 'simple'

    #配置类可以定义 init_app() 类方法，其参数是程序实例。在这个方法中，可以执行对当前环境的配置初始化。现在，基类 Config 中的 init_app() 方法为空
    @staticmethod
    def init_app(app):
        pass

#子类分别定义专用的配置,在 3 个子类中， SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。这样程序就可在不同的配置环境中运行，每个环境都使用不同的数据库。
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'zhihu-data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#config 字典中注册了不同的配置环境，而且还注册了一个默认配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}