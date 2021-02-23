from datetime import datetime, timedelta

from flask_restx import fields
from api_config import api

create_password_serializer = api.model('PasswordGenerate', {
    'id': fields.Integer(readonly=True),
    'expiration_access_range': fields.Integer(required=True, description='Expire access range.'),
    'expiration_date': fields.DateTime(required=True,
                                       description='Password expiration date.'),
    'password_size': fields.Integer(required=True),
    'randomize_range': fields.Integer(required=True)
})
