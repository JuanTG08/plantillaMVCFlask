from config.conexionDatabase import conexionDatabase
from models.entities.userEntity import userEntity
class userModel:
    table = 'user'
    @classmethod
    def getUserByLogin(self, conn, user):
        response = False
        sql = f"SELECT * FROM {self.table} WHERE username='{user.username}';"

        connCursor = conexionDatabase.getCursor(conn)

        if connCursor is not False:
            cursor = connCursor[1]
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                response = userEntity(row[0], row[1], userEntity.checkPassword(row[2], user.password), row[3])
            conexionDatabase.closeCursor(connCursor)
        return response
    @classmethod
    def getUserById(self, conn, id):
        response = False
        sql = f"SELECT id, username, fullname FROM {self.table} WHERE id={id}"
        connCursor = conexionDatabase.getCursor(conn)
        if connCursor is not None:
            cursor = connCursor[1]
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                response = userEntity(row[0], row[1], None, row[2])
            conexionDatabase.closeCursor(connCursor)
        return response