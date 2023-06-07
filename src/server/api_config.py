"""
api_config.py

Defines the APIConfig class which is a dictionary
containing every json retrieved from the BDE API.
"""

#-------------------------------------------------------------------#

import decimal
import os
import json
import requests

#-------------------------------------------------------------------#

class APIConfig(dict):
    """
    A dictionary containing every json retrieved from the BDE API.
    """
    def __init__(self, app=None) -> None:
        super().__init__()
        self.app = app
        self.loggers = app.loggers
        self.loggers.log.info("Retrieving API config...")

        self.load("config")

        self.loggers.log.info("API config retrieved.")

    def get_api_config(self) -> dict:
        """
        Retrieves the API config from the BDE API.
        """
        try:
            api_config = requests.get("https://fouaille.bde-tps.fr/api/product",
                                      timeout=5)
            api_config.raise_for_status()

        except requests.exceptions.HTTPError as err:
            self.loggers.log.error(err)
            return {}
        return api_config.json(parse_float=decimal.Decimal)

    def load(self, file_name:str=None) -> None:
        """
        Loads the json file.
        """
        if file_name is None:
            return

        with open(os.path.join(os.getcwd(),"data","json", "api", f"{file_name}.json"),
                  'r',
                  encoding="utf-8") as file:
            json_content = file.read()

        try:
            self.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            self.app.close()
