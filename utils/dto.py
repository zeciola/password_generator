from database_config import db


class DatabaseManager:

    def add_model(self, model_data):
        db.session.add(model_data)
        db.session.commit()

    def delete_model(self, model_data):
        db.session.delete(model_data)
        db.session.commit()

    def update_model(self):
        db.session.commit()

    def select_model(self, model, identifier):
        return model.query.filter_by(**identifier).first()


class PasswordGenerateDTO(DatabaseManager):
    def __init__(self):
        super().__init__()

    def get_password_by_uuid(self, model, uuid):
        return self.select_model(model=model, identifier=uuid)

    def remove_expired_password(self):
        ...

    def create_generate_password(self, model_data):
        self.add_model(model_data=model_data)
