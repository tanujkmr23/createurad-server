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
    SQLALCHEMY_DATABASE_URI = 'postgresql://zipcontyxiniyd:ea273ec958f1091fa79d99625bfec5b5203488e2a1a227c1252c91957c832159@ec2-18-211-97-89.compute-1.amazonaws.com:5432/d2mhlrm03h9r0n'
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
