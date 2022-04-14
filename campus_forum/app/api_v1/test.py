from . import api
from app import db, models

@api.route('/hello/')
def hello():
    return 'Hello'


