from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user
from models.userModel import userModel
from models.entities.userEntity import userEntity

class userController:
    @classmethod
    def loginFormulario(self):
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        return render_template('auth/Login.html')
    @classmethod
    def loginProccess(self, conn, request):
        if current_user.is_authenticated:
            return redirect(url_for('home'))

        userName = request.form['username']
        password = request.form['password']

        if userName != "" and password != "":
            user = userModel.getUserByLogin(conn, userEntity(0, userName, password, ""))
            if user is not False:
                if user.password: # Si la contraseña coinciden entonces...
                    login_user(user)
                    return redirect(url_for('home'))
                flash("Usuario o contraseña Incorrecta!")
            else:
                flash("Usuario o contraseña Incorrecta!_")
        else:
            flash("Campos en blanco.")
        return redirect('/login')
    @classmethod
    def loadUser(self, conn, id):
        return userModel.getUserById(conn, id)