from controllers.errorController import errorController

class routerError:
    @classmethod
    def error400(self, error):
        return errorController.redirectInit() # Bad request 400
    @classmethod
    def error401(self, error):
        return errorController.redirectInit() # Unauthorized access 401
    @classmethod
    def error404(self, error):
        return errorController.error404() # Not found 404
    @classmethod
    def error405(self, error):
        return errorController.redirectInit() # Method not allowed