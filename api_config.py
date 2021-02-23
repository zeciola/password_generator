from http import HTTPStatus

from flask import Blueprint
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          version='1.0',
          title='Password Manager',
          description='Password Manager API')


@api.errorhandler
def default_error_handler(error):
    return {'message': 'unhandled error occurred.'
            }, HTTPStatus.INTERNAL_SERVER_ERROR


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(error):
    return {'message': 'result not found on database'}, HTTPStatus.BAD_REQUEST
