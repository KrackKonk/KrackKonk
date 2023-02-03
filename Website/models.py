from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    data = db.Column(db.String(10000))
    sate = db.Column(db.DateTime(timezone= True), default= func.now())
    user_id = db.Column(db.Integer, db.models.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True )
    email=db.Column(db.String(150), unique =True)
    password=db.Column(db.string(150))
    first_name=db.Column(db,Column)
    notes = db.relationship('Note')
