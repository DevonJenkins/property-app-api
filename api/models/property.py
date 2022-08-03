from datetime import datetime 
from api.models.db import db

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    
    items = db.relationship("Item", cascade='all')

    def __repr__(self):
      return f"Property(`{property.id}`, {property.name}'"

#    def serialize(self):
#      property = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#      return property

    def serialize(self): 
      property = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      items = [item.serialize() for item in self.items]
      property['items'] = items 
      return property 
