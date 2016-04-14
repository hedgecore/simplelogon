import os


#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xc5zy\xd0\x813\xee\x97\x03\xec4l\xa0|\x9eYtg\x18\xe5\x8c\x8d\xc4s'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
