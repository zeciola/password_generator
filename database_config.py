from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def configure_database(app):
    db.init_app(app=app)
    migrate.init_app(app)
