from database.db import get_connection
from .entities.User import User

class UserModel():
    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"Users\" ORDER BY \"userName\" ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"Users\" WHERE \"userId\" = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO \"Users\" (\"userName\", \"userPwd\") 
                               VALUES(%s, %s);""", (user.userName, user.userPwd))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE \"Users\" SET \"userName\" = %s, \"userPwd\" = %s 
                                WHERE \"userId\" = %s""", (user.userName, user.userPwd, user.userId))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM \"Users\" WHERE \"userId\" = %s", (user.userId,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)