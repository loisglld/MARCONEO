"""
DataBase.py

Defines the DataBase class and everything 
related to the connexion to the database.
"""

#-------------------------------------------------------------------#

import mysql.connector as mysql

#-------------------------------------------------------------------#

class DataBase:
    """ 
    Defines the objects of type cursors that point on the MySQL database.
    It will be able to return information or modify values in the database.
    """

    def __init__(self, logs, logins:dict):
        """
        DataBase's constructor.
        """
        self.loggers = logs
        self.connexion = None
        host, database, user, password, port = logins.values()

        self.loggers.log.info("Connecting to the database...")
        try:           
            self.connexion = mysql.connect(host=host,
                                      database=database,
                                      user=user,
                                      password=password,
                                      port=port)
        except:
            self.logs.log.warning("Unable to connect to the database.")
            exit(1)
            
        self.cursor = self.connexion.cursor()
    
    def close(self):
        """
        Ferme la session MySQL.
        """    
        self.cursor.close()
        self.connexion.close()
        self.loggers.log.info("Disconnected from the database.")
        