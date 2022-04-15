from controllers.requestController import requestController

class routerRequest:
    def __init__(self, funcInternals):
        app = funcInternals.app

        @app.before_request
        def before_request_func():
            requestController.before_request()