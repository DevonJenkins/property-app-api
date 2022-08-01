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

@properties.route('/', methods=["GET"])
def index():
  properties = Property.query.all()
  return jsonify([property.serialize() for property in properties]), 200

@properties.route('/<id>', methods=["GET"])
def show(id):
  property = Property.query.filter_by(id=id).first()
  property_data = property.serialize()
  return jsonify(property=property_data), 200



