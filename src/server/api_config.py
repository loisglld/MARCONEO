"""
api_config.py

Defines the APIConfig class which is a dictionary
containing every json retrieved from the BDE API.
"""

#-------------------------------------------------------------------#

import decimal
import requests

#-------------------------------------------------------------------#

class APIJsons:
    """
    A dictionary containing every json retrieved from the BDE API.
    """
    def __init__(self, config_manager=None) -> None:
        super().__init__()
        self.config_manager = config_manager
        self.loggers = config_manager.app.loggers
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

    def retrieve_categories(self) -> list:
        """
        Retrieves the categories from the API.
        """
        return [product_type["type"] for product_type in self.categories_json]

    def setup_jsons(self) -> None:
        """
        Setup the jsons.
        """
        self.config_manager.generate_json("config",
                           self.get_api("https://fouaille.bde-tps.fr/api/product/index"),
                           api=1)
        self.config_json = self.config_manager.load("config", api=1)
        self.config_manager.generate_json("categories",
                           self.get_api("https://fouaille.bde-tps.fr/api/productType/index"),
                           api=1)
        self.categories_json = self.config_manager.load("categories", api=1)
