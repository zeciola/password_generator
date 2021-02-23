from datetime import datetime
from http import HTTPStatus
from uuid import uuid4

from flask_restx import Resource

from api_config import api
from models.password_gen import PasswordModel
from password_engine import PasswordGenerator
from serializers.password_gen import create_password_serializer
from utils.dto import PasswordGenerateDTO

password_gen_namespace = api.namespace(
    'generate_password', description='Generate password'
)

password_namespace = api.namespace(
    'password', description='Get generated password.'
)


@password_gen_namespace.route('/')
class PasswordGeneratorView(Resource):

    @api.doc('Generate password')
    @api.expect(create_password_serializer, validete=True)
    def post(self):
        payload = api.payload

        payload['password'] = PasswordGenerator(
            size=payload.pop('password_size'),
            randomize_pass_base=payload.pop('randomize_range')
        ).password_generate()

        uuid = str(uuid4())
        payload['uuid'] = uuid
        payload['expiration_date'] = datetime.strptime(
            payload['expiration_date'], '%Y-%m-%dT%H:%M:%S.%fZ')

        model_data = PasswordModel(**payload)
        PasswordGenerateDTO().create_generate_password(model_data=model_data)

        password_url = api.base_url + 'password/' + uuid
        return {'password_url': password_url}, HTTPStatus.CREATED


@password_namespace.route('/<uuid>')
@password_namespace.param('uuid', 'Generated password uuid')
class PasswordView(Resource):

    def _validate_password(self, model):
        validate_date = model.expiration_date >= datetime.now()
        validate_range = model.expiration_access_range > 0
        return validate_range and validate_date

    @api.doc('Get password')
    def get(self, uuid: str):
        dto = PasswordGenerateDTO()
        uuid = {'uuid': uuid}
        model = dto.select_model(PasswordModel, uuid)
        if not model:
            return {'error': 'UUID not found'}, HTTPStatus.NOT_FOUND

        if self._validate_password(model):
            model.expiration_access_range -= 1
            dto.update_model()
            password = model.password
            return {'password': password,
                    'expiration_access_range': model.expiration_access_range,
                    'expiration_date': datetime.strftime(model.expiration_date, '%d-%m-%Y %H:%M')
                    }

        return {'message': 'password was expired.'}, HTTPStatus.FORBIDDEN
