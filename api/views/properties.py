from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.property import Property
from api.models.item import Item

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

@properties.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  property = Property.query.filter_by(id=id).first()

  if property.profile_id != profile["id"]:
    return 'Forbidden', 403
  for key in data:
    setattr(property, key, data[key])
  
  db.session.commit()
  return jsonify(property.serialize()), 200

@properties.route("/<id>", methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  property = Property.query.filter_by(id=id).first()

  if property.profile_id != profile["id"]:
    return 'Forbidden', 403 

  db.session.delete(property)
  db.session.commit()
  return jsonify(message="Success"), 200

@properties.route('/<id>/items', methods=["POST"])
@login_required 
def add_item(id):
  property = Property.query.filter_by(id=id).first()
  profile = read_token(request)    

  data = request.get_json()
  data["property_id"] = id 
  data["profile_id"] = property.profile_id 
  
  if property.profile_id != profile["id"]:
    return 'Forbidden', 403

  item = Item(**data)

  db.session.add(item)
  db.session.commit()
  
  property_data = property.serialize()
  
  return jsonify(property_data), 201

@properties.route('/<property_id>/items', methods=["GET"])
def item_index(property_id):

  items = Item.query.all()
  return jsonify([item.serialize() for item in items]), 200

@properties.route('/<property_id>/items/<id>', methods=["GET"])
def item_show(property_id, id):
  item = Item.query.filter_by(id=id).first()
  item_data = item.serialize()

  return jsonify(item=item_data), 200


@properties.route("/<property_id>/items/<id>", methods=["DELETE"])
@login_required
def item_delete(property_id, id):
  profile = read_token(request)
  item = Item.query.filter_by(id=id).first()

  if item.profile_id != profile["id"]:
    return 'Forbidden', 403 

  db.session.delete(item)
  db.session.commit()
  return jsonify(message="Success"), 200
