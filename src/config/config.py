class Config():
    SECRET_KEY = 'IOAMSIODM!{**a'
class developmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask-login'
config = {
    "devConfig": developmentConfig
}