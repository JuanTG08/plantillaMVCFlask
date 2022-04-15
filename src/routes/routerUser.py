from flask import redirect, request
from flask_login import logout_user
from controllers.userController import userController

class routerUser:
    def __init__(self, funcInternals):
        app = funcInternals.app
        conn = funcInternals.db
        login_manager_app = funcInternals.loginManager

        @login_manager_app.user_loader
        def load_User(id):
            return userController.loadUser(conn, id)
        
        @app.route('/login', methods=['GET'])
        def loginFormulario():
            return userController.loginFormulario()
        
        @app.route('/loginProccess', methods=['POST'])
        def loginProccess():
            return userController.loginProccess(conn, request)
        
        @app.route('/logout')
        def logout():
            logout_user()
            return redirect('/login')

        '''
        @app.before_request
        def before_request_func():
            print("before_request executing!")
        '''