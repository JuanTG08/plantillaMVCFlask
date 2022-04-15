from flask_mysqldb import MySQL
class conexionDatabase:
    '''
    def __init__(self, app):
        try:
            db = MySQL(app)
            conn = db.connect()
            self.db = db
        except Exception as ex:
            print("Error connecting to database")
            raise Exception(ex)
    '''
    def __init__(self, app):
        db = MySQL(app)
        self.db = db
    @classmethod
    def getCursor(self, mysql):
        try:
            conn = mysql.connection
            return (conn, conn.cursor())
        except Exception as ex:
            # Evento de emergencia al no estar activa la DB
            print(" * Database don't run correctly")
            return False
    @classmethod
    def closeCursor(self, conn) -> None:
        conn[1].close()
        conn[0].commit()