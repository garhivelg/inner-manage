import os


class Config(object):
    """
    Common configuration
    """
    BASE_DIR = os.path.abspath(os.path.curdir)
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, "templates")
    STATIC_FOLDER = os.path.join(BASE_DIR, "static")
    LOGFILE = 'manage.log'


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    EXPLAIN_TEMPLATE_LOADING = True


class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
