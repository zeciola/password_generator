from unittest import TestCase
from app import create_app
from database_config import db


class PasswordGeneratorViewTest(TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.db = db.get_db()

    def test_generate_password(self):
        payload = {
          "expiration_access_range": 0,
          "expiration_date": "2021-02-22T19:53:40.033Z",
          "password_size": 0,
          "randomize_range": 0
        }
        ...