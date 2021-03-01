import os
from secrets import token_hex

BASDIR = os.path.dirname(__file__)

password = ''
with open(f'{BASDIR}/password.txt', 'r', encoding='utf-8') as f:
    password = f.readline()


# SQLALCHEMY_DATABASE_URI = os.path.join(BASEDIR,'sqlite:///temp/app.db')

class DevelopmentConfig(object):
    """ Write your development configuration here"""
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = f"postgresql://orinda:{password}@localhost/blog1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = token_hex(40)


class ProductionConfig(object):
    """ Write your production configuration here"""
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///temp/app.db'


config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
