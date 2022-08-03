from datetime import datetime 
from api.models.db import db 

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

def __repr__(self):
  return f"Item(`{self.id}`, `{self.name}`)"
  
def serialialize(self):
  item = {c.name: getattr(self, c.name) for c in self.__table__.columns}
  return item 
