import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = "!!!SECRET_KEY!!!!!"

class ProdConfig(Config):
    DEBUG = False
    DEBUG_TB_INTERCEPT_REDIRECTS = True

    SQLALCHEMY_DATABASE_URI = "mysql://USER:PASSWORD@localhost/DATABASE"
    SQLALCHEMY_POOL_TIMEOUT = 30

    CACHE_TYPE = "memcached"

    STATIC_FOLDER = "dist"
    TEMPLATE_FOLDER = "dist"

class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0

    WTF_CSRF_TIME_LIMIT = 10000

    SQLALCHEMY_DATABASE_URI = "mysql://USER:PASSWORD@localhost/DATABASE"
    SQLALCHEMY_POOL_TIMEOUT = 30

    CACHE_TYPE = "memcached"

    STATIC_FOLDER = "static"
    TEMPLATE_FOLDER = "templates"

    PORT = "5001"
    HOST = "127.0.0.1"

