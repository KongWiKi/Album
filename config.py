'''
@author：KongWeiKun
@file: config.py
@time: 17-12-31 上午11:29
@contact: 836242657@qq.com
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """基础配置类"""
    SECRET_KEY='42ehhdswqrry9wqry298f29tygh3qt'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_MAIL_SUBJECT_PREFIX = u'[猪猪相册]'
    FLASK_MAIL_SENDER = 'kongwiki@163.com'
    FLASK_ADMIN = 'kongwiki@163.com'
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/app/static/img/'
    FANXIANGCE_COMMENTS_PER_PAGE = 15
    FANXIANGCE_ALBUMS_PER_PAGE = 12
    FANXIANGCE_PHOTOS_PER_PAGE = 20
    FANXIANGCE_ALBUM_LIKES_PER_PAGE = 12
    FANXIANGCE_PHOTO_LIKES_PER_PAGE = 20
    FANXIANGCE_FOLLOWERS_PER_PAGE = 10
    BOOTSTRAP_SERVE_LOCAL = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    MAIL_SERVER = 'smtp.163.com',
    MAIL_PROT = 465,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'kongwiki@163.com',
    MAIL_PASSWORD = 'hhxxttxs0214',
    MAIL_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class HerokuConfig(Config):
    MAIL_SERVER = 'smtp.163.com',
    MAIL_PROT = 465,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'kongwiki@163.com',
    MAIL_PASSWORD = 'hhxxttxs0214',
    MAIL_DEBUG = True  # os.environ.get('MAIL_PASSWORD')
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



config = {
    'development' : DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}