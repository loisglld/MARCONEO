"""
MarcoNeo.py

Defines MarcoNeo's app class.
MarcoNeo class encapsulates the whole logic of the application
as well as the connections to the database and the RFID reader.
"""

#-------------------------------------------------------------------#

from SRC.Loggers import Loggers
from SRC.DataBase import DataBase
from SRC.INTERFACE.GUI import GUI

import os
import json
import decimal

#-------------------------------------------------------------------#

class MarcoNeo:
    """
    MarcoNeo's app class.
    MarcoNeo class encapsulates the whole logic of the application
    as well as the connections to the database and the RFID reader.
    """

    NAME = "MARCONEO"
    VERSION = "0.6.0"

    def __init__(self):
        """
        MarcoNeo's app class's constructor.
        """
        # Setup the logger
        self.loggers = Loggers(MarcoNeo.NAME)
        self.loggers.log.info("Starting MarcoNeo v" + MarcoNeo.VERSION + "...")
        
        # Setup config
        self.config = self.setup_config()
        self.default_config = self.config 
        
        # Setup the database
        self.conn_info = self.get_pwd()
        self.db = DataBase(self.loggers, self.conn_info)

        # Setup the GUI
        self.gui = GUI(self)
        self.gui.protocol("WM_DELETE_WINDOW", self.close)
        
        self.loggers.log.info("MarcoNeo launched.")
        self.gui.start()
        
    def setup_config(self):
        """
        Reads the json file (./config.json).
        Shuts down the process if an error occurs.
        
        The json file is used to configure the images and the shopping menus
        (items, prices, etc.)
        """
        
        file_object = open(os.path.join("DATA", "config.json"), "r")
        json_content = file_object.read()
        file_object.close()
        
        try:
            config = json.loads(json_content, parse_float=decimal.Decimal)
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warn(f"Error while parsing the config.json file at line {decode_err.lineno}")
            quit()
            
        return config
        
    def get_pwd(self):
        pwd_path = os.path.join(os.path.abspath(os.getcwd()),'pwd.txt')
        with open(pwd_path, 'r') as f:
            lines = f.readlines()
            conn_info = {'host': lines[0].strip(),
                        'database': lines[1].strip(),
                        'user': lines[2].strip(),
                        'password': lines[3].strip(),
                        'port': int(lines[4].strip()),
                        }
        return conn_info
      
    def close(self):
        """
        Quits the application.
        """
        # Close the database connection safely
        for i in range(5):
            try:
                self.db.close()
                break
            except:
                self.loggers.log.warn("Error while closing the database connection. Retrying...")
        else:
            self.loggers.log.error("Could not close the database connection after 5 attempts.")

        # Close the rest of the application
        self.gui.close()
        self.loggers.log.info("Closing MARCONEO...")
        self.loggers.close()
