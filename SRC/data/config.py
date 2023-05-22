"""
config.py

Contains the config class.
Contains the config class which is
used to store the configuration data
of the application.
"""

#-------------------------------------------------------------------#

import json
import os
import decimal

#-------------------------------------------------------------------#

class Config(dict):
    """
    Stores the configuration data of the application.
    """
    def __init__(self, app) -> None:
        """
        Reads the json file (./config.json).
        Shuts down the process if an error occurs.

        The json file is used to configure the images and the shopping menus
        (items, prices, etc.)
        """
        self.loggers = app.loggers

        with open(os.path.join(os.getcwd(),"DATA", "config.json"), 'r', encoding="utf-8") as f:
            json_content = f.read()

        try:
            self.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            app.close()
