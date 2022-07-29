from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.property import Property

properties = Blueprint('properties', 'properties')

@properties.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  property = Property(**data)
  db.session.add(property)
  db.session.commit()
  return jsonify(property.serialize()), 201
