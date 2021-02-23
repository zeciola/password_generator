import os

from dotenv import load_dotenv
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from api_config import api
from database_config import configure_database
from views.password import password_gen_namespace, password_namespace


def create_app():
    load_dotenv(verbose=True)

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config['RESTX_VALIDATE'] = os.getenv('RESTX_VALIDATE', True)
    app.config['ERROR_404_HELP'] = os.getenv('ERROR_404_HELP', False)

    user = os.getenv('USER_DB', 'root')
    password = os.getenv('POSTGRES_PASSWORD', 'KDc~*HtHw-XL*&45Kp:go(?0.i@MOL')
    database = os.getenv('DATABASE', 'password_generator_db')
    port = os.getenv('PORT', '5432')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{user}:{password}@database:{port}/{database}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_database(app)
    api.add_namespace(password_namespace)
    api.add_namespace(password_gen_namespace)
    return app
