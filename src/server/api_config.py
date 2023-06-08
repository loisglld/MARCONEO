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

class APIJsons:
    """
    A dictionary containing every json retrieved from the BDE API.
    """
    def __init__(self, app=None) -> None:
        super().__init__()
        self.app = app
        self.loggers = app.loggers
        self.loggers.log.info("Retrieving API config...")
        self.config_json, self.categories_json = {}, {}

        self.setup_jsons()

        self.categories = self.retrieve_categories()

        self.loggers.log.info("API configurations files retrieved.")

    def get_api(self, url) -> dict:
        """
        Retrieves the API config from the BDE API.
        """
        try:
            api_config_resp = requests.get(url,
                                      timeout=5)
            api_config_resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self.loggers.log.error(err)
            return {}
        return api_config_resp.json(parse_float=decimal.Decimal)

    def generate_json(self, name,  json_retrieved:json) -> bool:
        """
        Generate a json file corresponding
        to the request response given.
        """
        with open(os.path.join(os.getcwd(),"data","json", "api", f"{name}.json"),
                  'w',
                  encoding="utf-8") as file:
            file.write(json.dumps(json_retrieved, indent=4))

    def load(self, file_name:str=None) -> dict:
        """
        Loads the json file.
        """
        if file_name is None:
            return
        dictionary = {}

        with open(os.path.join(os.getcwd(),"data","json", "api", f"{file_name}.json"),
                  'r',
                  encoding="utf-8") as file:
            json_content = file.read()

        try:
            dictionary.update(json.loads(json_content, parse_float=decimal.Decimal))
        except json.JSONDecodeError as decode_err:
            self.loggers.log.warning("Error while parsing the config.json file at line %s",
                                     decode_err.lineno)
            self.app.close()

        return dictionary

    def retrieve_categories(self) -> list:
        """
        Retrieves the categories from the API.
        """
        return [product_type["type"] for product_type in self.categories_json["product_type"]]

    def setup_jsons(self) -> None:
        """
        Setup the jsons.
        """
        self.generate_json("config",
                           self.get_api("https://fouaille.bde-tps.fr/api/product/index"))
        self.config_json = self.load("config")
        self.generate_json("categories",
                           self.get_api("https://fouaille.bde-tps.fr/api/productType/index"))
        self.categories_json = self.load("categories")