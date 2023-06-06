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

        with open(os.path.join(os.getcwd(),"data", "config.json"),
                  'r',
                  encoding="utf-8") as file:
            json_content = file.read()

        try:
            self.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            app.close()

        self.default_config = self.copy()

    def change_price(self, toggle, item_name, new_price):
        """
        Changes the price of an item.
        """
        items = self["Shopping"][toggle]['items']
        for index, item in enumerate(items):
            if item['name'] == item_name:
                items[index]['price'] = decimal.Decimal(new_price)
                break
