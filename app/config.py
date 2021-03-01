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
    # SQLALCHEMY_DATABASE_URI = f"postgresql://username:{password}@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = token_hex(40)


class ProductionConfig(object):
    """ Write your production configuration here"""
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///temp/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = token_hex(40)


config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
