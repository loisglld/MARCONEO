"""
dbcursor.py

Defines the DBCursor class and everything
related to the connexion to the database.
"""

#-------------------------------------------------------------------#

import mysql.connector as mysql

from src.utils.decorators import close_service, setup_service
from src.data.member import Member
from src.data.logins import Logins

#-------------------------------------------------------------------#

class DBCursor:
    """
    Defines the objects of type cursors that point on the MySQL database.
    It will be able to return information or modify values in the database.
    """
    def __init__(self, app) -> None:
        """
        DataBase's constructor.
        """
        self.loggers = app.loggers
        self.connection = None
        self.cursor = None
        self._logins = Logins()
        self.connect_to_db()

    @setup_service(max_attempts=5)
    def connect_to_db(self) -> bool:
        """
        Connects to the database.
        """
        self.connection = mysql.connect(host=self._logins.get_host(),
                                        database=self._logins.get_database(),
                                        user=self._logins.get_user(),
                                        password=self._logins.get_password(),
                                        port=self._logins.get_port())
        self.cursor = self.connection.cursor()
        self.loggers.log.info("Connected to the database.")
        return True

    @close_service
    def close(self) -> bool:
        """
        Ferme la session MySQL.
        """
        self.connection.close()
        self.loggers.log.debug("Disconnected from the database.")
        return True

    def get_member(self, card_id:int) -> Member:
        """
        Retrieves a user with the given ID from the database.
        Returns the user if a match is foundin the database, None otherwise
        """
        if card_id < 0:
            return None

        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

        self.cursor.execute("""SELECT first_name, last_name, nickname, card_id,\
                            balance, isadmin, iscontributor
                                FROM Member
                                WHERE card_id = %s""", (card_id,))

        result = self.cursor.fetchone()

        if result is not None:
            member_data = {'first_name': result[0],
                        'last_name': result[1],
                        'nickname': result[2],
                        'card_id': result[3],
                        'balance': result[4],
                        'is_admin': result[5],
                        'is_contributor': result[6]}
            self.loggers.log.debug(f"Retrieving member {member_data['first_name']} (ID:{card_id})")
            return Member(self.loggers, member_data)
        else:
            self.loggers.log.warn(f"No member found with card ID {card_id}")
            return None

    def update_balance(self, member:Member) -> None:
        """
        Updates the balance of the given member in the database.
        """
        if member is None:
            return

        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

        self.cursor.execute("""UPDATE Member
                            SET balance = %s
                            WHERE card_id = %s""", (member.balance, member.card_id))
        self.connection.commit()

        self.loggers.log.debug(f"Member {member.first_name} (ID:{member.card_id}) Balance: {member.balance}")
