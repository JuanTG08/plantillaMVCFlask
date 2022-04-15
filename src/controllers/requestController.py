from flask import redirect, url_for
from flask_login import current_user

class requestController:
    @classmethod
    def before_request(self):
        if current_user.is_authenticated:
            print("wtf")
            return redirect(url_for('home'))