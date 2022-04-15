from flask_login import login_required
from controllers.homeController import homeController

class routerHome:
    def __init__(self, app):
        @app.route('/')
        def index():
            return homeController.index()
        
        @app.route('/home')
        @login_required
        def home():
            return homeController.home()