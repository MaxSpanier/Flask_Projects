import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    # Save secret key somewhere safe
    pass

class DevelopmentConfig(Config):
    TESTING = True
    SECRET_KEY = '\xc5\xde=\xf4Q\x08)\xd0\xfcT\x1d*D\x1aQ\xd3\xb4\x80s\x8b\xc4R\x08\xd8'
