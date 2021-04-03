import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from src.app import create_app, db

from src.models import UniversityModel



env_name = os.environ.get('FLASK_ENV')
print('env_name : ', env_name)
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()