from flask import redirect, render_template


class errorController:
    @classmethod
    def redirectInit(self):
        return redirect('/')
    @classmethod
    def error404(self):
        return render_template('error/error404.html'), 404