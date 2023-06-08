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

from src.server.api_config import APIJsons

#-------------------------------------------------------------------#

class Config:
    """
    Stores the configuration data of the application.
    """
    DEFAULT = "default"
    CUSTOM = "custom"
    def __init__(self, app) -> None:
        """
        Reads the json file (./config.json).
        Shuts down the process if an error occurs.

        The json file is used to configure the images and the shopping menus
        (items, prices, etc.)
        """
        self.loggers = app.loggers
        self.app = app

        self.api_config = APIJsons(app)
        self.default_config = self.load(self.DEFAULT)
        self.name = self.DEFAULT
        self.loaded_config = {}
        self.initial_config = {}

    def load(self, file_name:str=None) -> dict:
        """
        Loads the json file onto loaded_config and copies it to initial_config.
        Returns a dictionary containing the json file data.
        """
        if file_name is None:
            return {}
        dictionary = {}
        with open(os.path.join(os.getcwd(),"data","json", f"{file_name}.json"),
                  'r',
                  encoding="utf-8") as file:
            json_content = file.read()
        try:
            dictionary.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            self.app.close()

        self.name = file_name
        self.loaded_config = dictionary.copy()
        self.initial_config = self.loaded_config.copy()
        return dictionary

    def change_price(self, toggle, item_name, new_price):
        """
        Changes the price of an item.
        """
        items = self.loaded_config["Shopping"][toggle]['items']
        for index, item in enumerate(items):
            if item['name'] == item_name:
                items[index]['price'] = decimal.Decimal(new_price)
                break
