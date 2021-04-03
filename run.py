import os

from src.app import create_app
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#if __name__ == '__main__':
env_name = os.environ.get('FLASK_ENV')
app = create_app(env_name)
application = app

"""
Uncomment the below line for local 
"""
#application.run(threaded=True)
