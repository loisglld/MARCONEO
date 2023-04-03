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
        self.loggers.log.debug("Disconnected from the database.")
        
    def get_member(self, card_id: int):
        """
        Retrieves a user with the given ID from the database.
        Returns the user if a match is foundin the database, None otherwise
        """
        if card_id < 0:
            return None
        
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        
        self.cursor.execute("""SELECT first_name, last_name, nickname, card_id, balance, isadmin, iscontributor
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
            self.loggers.log.debug(f"Retrieving member {member_data['first_name']} {member_data['last_name']} (ID:{card_id})")
            return Member(self.loggers, member_data)
        else:
            self.loggers.log.warn(f"No member found with card ID {card_id}")
            return None
        
    def purchase_cart(self, member: Member):
        """
        Confirms the purchase of a member.
        """
        if member is None:
            return
        
        self.cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
        
        self.cursor.execute("""UPDATE Member
                            SET balance = %s
                            WHERE card_id = %s""", (member.balance, member.card_id))
        self.connexion.commit()
        
        self.loggers.log.debug(f"Member {member} has purchased {member.cart.items.__str__()}")
        