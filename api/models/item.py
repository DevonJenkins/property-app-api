from datetime import datetime 
from api.models.db import db 

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now(tz=None))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))

    def __repr__(self):
      return f"Item(`{self.id}`, `{self.name}`)"
    
    def serialize(self):
      return {
        "id": self.id,
        "name": self.name, 
        "property_id": self.property_id,
   #     "date": self.date.strftime('%Y-%m-%y'),
          } 
