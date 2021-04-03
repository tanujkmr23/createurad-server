from flask import request, json, Response, Blueprint, jsonify
from ..models.UniversityModel import UniversityModel, UniversitySchema
from flask_cors import CORS

university_api = Blueprint('university_api', __name__)
CORS(university_api)
university_schema = UniversitySchema()

@university_api.route('/filter', methods=['POST'])
def get_filtered_university():
    """
    API to get all the filtered university with pagination
    """
    payload = request.json

    universities = UniversityModel.get_filterd_university(payload)
    ser_university = university_schema.dump(universities.items, many=True)
    results = {
        'items': ser_university,
        'has_next': universities.has_next,
        'has_prev': universities.has_prev,
        'page': universities.page,
        'pages': universities.pages,
        'prev_num': universities.prev_num,
        'next_num': universities.next_num,
        'total': universities.total
    }
    return custom_response(results, 200)

@university_api.route('/create_or_update', methods=['POST'])
def create_or_update_university():
    """
    API to create University
    """
    req_data = request.json
    payload = {}
    if 'id' in req_data:
        payload['id'] = req_data['id']
    if 'domain' in req_data:
        payload['domain'] = req_data['domain']
    
    if 'id' in req_data:
        university = UniversityModel.get_university_by_id(req_data['id'])
        UniversityModel.update(university, data=req_data)
        return custom_response({'success': True}, 201)

    university = UniversityModel(
        alpha_two_code=req_data['alpha_two_code'], country=req_data['country'], domain=req_data['domain'],
        name=req_data['name'], web_page=req_data['web_page']
    )
    university.save()
    return custom_response({'success': True}, 201)

@university_api.route('/delete', methods=['POST'])
def delete_university():
    """
    API to delete University
    """
    req_data = request.json
    university = UniversityModel.get_university_by_id(req_data['id'])
    if university:
        university.delete()
        return custom_response({'success': True}, 201)
    return custom_response({'success': False}, 400)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )