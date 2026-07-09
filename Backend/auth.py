from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id


USERNAME = "admin"
PASSWORD = "admin123"


def validate_user(username, password):
    return username == USERNAME and password == PASSWORD