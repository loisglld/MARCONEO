"""
DataBase.py

Defines the DataBase class and everything 
related to the connexion to the database.
"""

#-------------------------------------------------------------------#

from SRC.DATABASE.Member import Member
import mysql.connector as mysql

#-------------------------------------------------------------------#

class DataBase:
    """ 
    Defines the objects of type cursors that point on the MySQL database.
    It will be able to return information or modify values in the database.
    """

    def __init__(self, loggers, logins:dict):
        """
        DataBase's constructor.
        """
        self.loggers = loggers
        self.connexion = None
        host, database, user, password, port = logins.values()
        
        self.loggers.log.debug("Connecting to the database...")
        try:           
            self.connexion = mysql.connect(host=host,
                                            database=database,
                                            user=user,
                                            password=password,
                                            port=port)
        except:
            self.loggers.log.warning("Unable to connect to the database.")
            exit(1)
        
        self.loggers.log.info("Connected to the database.")
        self.cursor = self.connexion.cursor()
    
    def close(self):
        """
        Ferme la session MySQL.
        """    
        self.cursor.close()
        self.connexion.close()
        self.loggers.log.info("Disconnected from the database.")
        
    def get_contributor(self, id: int):
        """
        Retrieves a user with the given ID from the database.
        Returns the user if a match is foundin the database, None otherwise
        """
        if id < 0:
            return None
        
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        
        self.cursor.execute("""SELECT first_name, last_name, nickname, card_id, balance, isadmin, iscontributor
                            FROM Cotisant
                            WHERE card_id = %s""", (id,))
        
        result = self.cursor.fetchone()
        
        if result is not None:
            member_data = {'first_name': result[0],
                        'last_name': result[1],
                        'nickname': result[2],
                        'card_id': result[3],
                        'balance': result[4],
                        'is_admin': result[5],
                        'is_contributor': result[6]}
            return Member(member_data)
        else:
            return None