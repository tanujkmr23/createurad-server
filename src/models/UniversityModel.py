from marshmallow import fields, Schema
from sqlalchemy import func
from . import db
import datetime

class UniversityModel(db.Model):
  """
  University Model
  """

  __tablename__ = 'university'

  """
  Table Column Definition
  """
  id = db.Column(db.Integer, primary_key=True)
  alpha_two_code = db.Column(db.String(2), nullable=False)
  country = db.Column(db.String(255), nullable=False)
  domain = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  web_page = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, alpha_two_code, country, domain, name, web_page):
    self.alpha_two_code = alpha_two_code
    self.country = country
    self.domain = domain
    self.name = name
    self.web_page = web_page
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()
    

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    print('data : ', data)
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  @staticmethod
  def get_all_university():
    return UniversityModel.query.all()

  @staticmethod
  def get_university_by_id(id):
    return UniversityModel.query.get(id)
  
  @staticmethod
  def get_filterd_university(payload):
    filters = None
    result_query = UniversityModel.query

    """
    Filter key for country code and domain that ends with .edu,.us etc
    """
    if payload['filter_key'] != '':
      try:
        payload['filter_key'].index('.')
      except: #if filter_key has no '.' then system will assume it as country code
        filters = func.lower(UniversityModel.alpha_two_code) == func.lower(payload['filter_key'])
      else:
        if payload['filter_key'].index('.') == 0: #if '.' is at first index
          filters = UniversityModel.domain.endswith(payload['filter_key'])
        else:
          filters = func.lower(UniversityModel.alpha_two_code) == func.lower(payload['filter_key'])

      result_query = result_query.filter(filters)
    """
    Filter by search key
    """
    if payload['search_key'] != '':
      result_query = result_query.filter(UniversityModel.name.ilike("%"+payload['search_key']+"%"))

    """
    Final paginated result
    """
    return result_query.paginate(page=payload['page'], per_page = payload['limit'], error_out=False)

  def __repr__(self):
    return '<id {}>'.format(self.id)

class UniversitySchema(Schema):
  """
  University Schema
  """
  id = fields.Int(dump_only=True)
  alpha_two_code = fields.Str(required=True)
  country = fields.Str(required=True)
  domain = fields.Str(required=True)
  name = fields.Str(required=True)
  web_page = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)