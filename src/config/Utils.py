from flask import redirect, url_for
from flask_login import current_user


class Utils:
    def __init__(self, app, db, loginManager) -> None:
        self.app = app
        self.db = db
        self.loginManager = loginManager