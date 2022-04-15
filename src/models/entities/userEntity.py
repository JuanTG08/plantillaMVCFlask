from werkzeug.security import check_password_hash
from flask_login import UserMixin

class userEntity(UserMixin):
    def __init__(self, id, username, password, fullname) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    @classmethod
    def checkPassword(self, encryptedPassword, password):
        return check_password_hash(encryptedPassword, password)