from flask import redirect, render_template, url_for
from flask_login import current_user


class homeController:
    @classmethod
    def index(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        return render_template('Inicio.html')
    @classmethod
    def home(self):
        return render_template('Home/Home.html')