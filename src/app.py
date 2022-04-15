# Importamos Flask
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from routes.routerError import routerError
from config.Utils import Utils
# Importamos la Conexion a la Base de Datos
from config import conexionDatabase, config

# Importamos las rutas que deseamos Utilizar
from routes import routerHome, routerUser, routerRequest # Importamos todas las rutas

# Establecemos las rutas para poder acceder a subcarpetas dentro de subcarpetas
import os, sys
paths = os.path.abspath('..')
sys.path.insert(1, paths)

class App: # Iniciamos la Clase APP
    app = Flask(__name__)
    csrf = CSRFProtect()
    login_manager_app = LoginManager(app)
    def __init__(self): # Inicio de las Rutas
        db = conexionDatabase.conexionDatabase(self.app).db

        funcInternals = Utils(self.app, db, self.login_manager_app)

        # routerRequest.routerRequest(funcInternals)
        routerHome.routerHome(self.app) # Ejecutamos las rutas "Home"
        routerUser.routerUser(funcInternals) # Ejecutamos las rutas "User"            
        
        # Manejo de Errores
        self.app.register_error_handler(400, routerError.error400)
        self.app.register_error_handler(401, routerError.error401)
        self.app.register_error_handler(404, routerError.error404)
        self.app.register_error_handler(405, routerError.error405)
    @classmethod
    def starApp(self): # Inicio del servidor
        self.app.config.from_object(config.config['devConfig'])
        self.csrf.init_app(self.app)
        self.app.run()