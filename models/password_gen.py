from database_config import db
from datetime import datetime


class PasswordModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expiration_access_range = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    expiration_date = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    uuid = db.Column(db.String(36), nullable=False)

    def __repr__(self):
        return f'<PasswordGenerate {self.id}>'
