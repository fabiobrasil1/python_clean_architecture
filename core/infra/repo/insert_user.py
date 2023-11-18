# pylint: disable=E1101
from core.infra.config import DBConnectionHandler
from core.infra.entities import Users

class InsertUserRepository:
    """ Insert User """

    @classmethod
    def insertUser(cls):
        with DBConnectionHandler() as db_connection:
            try:
                newUser = Users(
                        name="fabio", 
                        password="12345"
                    )
                db_connection.session.add(newUser)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
