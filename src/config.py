import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://creatsurad:creatsurad@localhost:5432/creatsuraddb'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    """SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')"""

app_config = {
    'development': Development,
    'production': Production,
}
