from flask import Flask
from flask_cors import CORS, cross_origin

from .config import app_config
from .models import db

# import university_api blueprint
from .views.UniversityView import university_api as university_blueprint


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  print('env_name :=> : ', env_name)
  print('app_config[env_name] :=> : ', app_config[env_name])
  # db initialization
  db.init_app(app)

  #university bluprint registration
  app.register_blueprint(university_blueprint, url_prefix='/api/v1/university')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Server is running'

  return app
