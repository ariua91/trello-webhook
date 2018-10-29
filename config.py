import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Cofing(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ';lkdsajfeoiwur438975fjds'



class ProductionConfig(Config):
    DEBUG = False


class StagingCongif(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
