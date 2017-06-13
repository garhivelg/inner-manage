class Config(object):
    """
    Common configuration
    """
    pass


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
