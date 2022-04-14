from datetime import datetime
from . import db



class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class user(BaseModel, db.Model):

    __tablename__ = "cf_user_profile"

    id = db.Column(db.Integer, primary_key=True, index=True)
    usid = db.Column(db.Integer, unique=True, nullable=False)



