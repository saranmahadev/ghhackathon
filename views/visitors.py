from flask import Blueprint,request
from modules.db import Db

visitor = Blueprint('visitor', __name__,url_prefix='/visitors')

@visitor.route('/fetch')
def count():
    try:
        with Db('visitors') as db:
            return {
                'status':'success',
                'count':len(db.findall()),
                'code':200
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': e,
            'code': 400
        }

@visitor.route('/add', methods = ['POST'])
def add():
    try:
        with Db('visitors') as db:
            db.insert(
                request.json
            )
            return {
                'status': 'success',
                'message': 'Visitor added successfully',
                'code': 200
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': e,
            'code': 400
        }