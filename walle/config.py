# -*- coding: utf-8 -*-
import os
from datetime import timedelta

class CommonConfig(object):
    """Base configuration."""
    VERSION = '2.0.1'

    SECRET_KEY = os.environ.get('WALLE_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    # 项目根路径
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Can be "memcached", "redis", etc.
    CACHE_TYPE = 'simple'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    LOGIN_DISABLED = False
    # 设置session的保存时间。
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    # 前端项目部署路径
    FE_PATH = os.path.abspath(PROJECT_ROOT + '/fe/') + '/'
    AVATAR_PATH = '/avatar/'
    UPLOAD_AVATAR = FE_PATH + AVATAR_PATH

    # 邮箱配置
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEFAULT_SENDER = 'service@walle-web.io'
    MAIL_USERNAME = 'service@walle-web.io'
    MAIL_PASSWORD = 'Ki9y&3U82'

    # 日志
    LOG_PATH = os.path.join(PROJECT_ROOT, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024

    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10
    LOG_FORMAT = "%(asctime)s %(thread)d %(message)s"

    # 登录cookie 防止退出浏览器重新登录
    COOKIE_ENABLE = False

class DevelopmentConfig(CommonConfig):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    HOST = 'debian'
    PORT = 5000
    SSL = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://walle:walle@localhost:3306/walle?charset=utf8'

    # 本地代码检出路径（用户查询分支, 编译, 打包） #TODO
    CODE_BASE = '/tmp/walle/codebase/'

    SQLALCHEMY_ECHO = True

    # 登录cookie 防止退出浏览器重新登录
    COOKIE_ENABLE = False

class ProductionConfig(CommonConfig):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_ECHO = False

    # 服务启动 @TODO
    # HOST 修改为与 nginx server_name 一致.
    # 后续在web hooks与通知中用到此域名.
    HOST = 'debian'
    PORT = 5000
    # https True, http False
    SSL = False

    # 数据库设置: 数据库驱动采用pymysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://walle:walle@localhost:3306/walle?charset=utf8'

    # 本地代码检出路径（用户查询分支, 编译, 打包)
    CODE_BASE = '/tmp/walle/codebase/'

    # 日志存储路径 @TODO
    # 默认为walle-web项目下logs, 可自定义路径, 需以 / 结尾
    # LOG_PATH = '/var/logs/walle/'
    LOG_PATH = os.path.join(CommonConfig.PROJECT_ROOT, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024

    # 邮箱配置 @TODO
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEFAULT_SENDER = 'service@walle-web.io'
    MAIL_USERNAME = 'service@walle-web.io'
    MAIL_PASSWORD = 'Ki9y&3U82'

    # 登录cookie 防止退出浏览器重新登录
    COOKIE_ENABLE = False


envrionment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
