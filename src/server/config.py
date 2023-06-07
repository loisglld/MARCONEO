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

from src.server.api_config import APIConfig

#-------------------------------------------------------------------#

class Config:
    """
    Stores the configuration data of the application.
    """
    DEFAULT = "default"
    def __init__(self, app) -> None:
        """
        Reads the json file (./config.json).
        Shuts down the process if an error occurs.

        The json file is used to configure the images and the shopping menus
        (items, prices, etc.)
        """
        self.loggers = app.loggers
        self.app = app

        self.base_config = None
        self.name = self.DEFAULT

        self.api_config = APIConfig(app)
        self.json = {}

        self.load(self.DEFAULT)

    def load(self, file_name:str=None) -> None:
        """
        Loads the config.json file.
        """
        if file_name is None:
            return

        self.name = file_name

        with open(os.path.join(os.getcwd(),"data","json", f"{file_name}.json"),
                  'r',
                  encoding="utf-8") as file:
            json_content = file.read()

        try:
            self.json.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            self.app.close()

        # Save the default config to be able to reset the config
        self.base_config = self.json.copy()

    def change_price(self, toggle, item_name, new_price):
        """
        Changes the price of an item.
        """
        items = self.json["Shopping"][toggle]['items']
        for index, item in enumerate(items):
            if item['name'] == item_name:
                items[index]['price'] = decimal.Decimal(new_price)
                break
