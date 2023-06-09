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

        self.api_config = APIJsons(self)
        self.name = self.DEFAULT
        self.loaded_config = {}
        self.initial_config = {}
        self.custom_config = {}

        self.setup_custom()
        self.default_config = self.load(self.DEFAULT)

    def generate_json(self, name, json_retrieved:json, api:bool=0) -> bool:
        """
        Generate a json file corresponding
        to the request response given.
        """
        if api:
            path = "api"
        else:
            path = ""

        with open(os.path.join(os.getcwd(),"data","json", path, f"{name}.json"),
                  'w',
                  encoding="utf-8") as file:
            file.write(json.dumps(json_retrieved, indent=4))

    def setup_custom(self) -> None:
        """
        Setup the custom config.
        """
        if os.path.exists(os.path.join(os.getcwd(),"data","json", "custom.json")):
            self.check_difference_with_config_api()
            return

        self.custom_config = self.load("config", api=1)

        # Add the selected bool parameter to the custom config
        for items in self.custom_config:
            for product in items["products"]:
                product["selected"] = False

        custom_data = {"data": self.custom_config}
        self.generate_json("custom", custom_data, api=0)
        self.cat_refill(self.custom_config)

    def load(self, file_name:str=None, api:bool=0) -> dict:
        """
        Loads the json file onto loaded_config and copies it to initial_config.
        Returns a dictionary containing the json file data.
        """
        if file_name is None:
            return {}
        dictionary = {}

        if api:
            path = "api"
        else:
            path = ""

        with open(os.path.join(os.getcwd(),"data","json", path, f"{file_name}.json"),
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
        self.loaded_config = dictionary["data"].copy()
        self.cat_refill(self.loaded_config)
        self.initial_config = self.loaded_config.copy()
        return dictionary["data"]

    def change_price(self, toggle, item_name, new_price):
        """
        Changes the price of an item.
        """
        items = self.loaded_config["Shopping"][toggle]['items']
        for index, item in enumerate(items):
            if item['name'] == item_name:
                items[index]['price'] = decimal.Decimal(new_price)
                break

    def cat_refill(self, config) -> None:
        """
        Concatenates the refill toggle to the loaded json.
        """
        with open(os.path.join(os.getcwd(),"data","json", "refill.json"),
                  'r',
                  encoding="utf-8") as file:
            refill_content = file.read()

        refill_dict = json.loads(refill_content, parse_float=decimal.Decimal)
        config.append(refill_dict['refill'])

    def get_loaded_categories(self) -> list:
        """
        Returns the categories of the loaded config.
        """
        return [product_type["product_type"] for product_type in self.loaded_config]

    def update_custom_file(self, list_of_items) -> None:
        """
        Adds every selected item to the custom config json.
        """
        self.custom_config = list_of_items
        json_created = {"data": self.custom_config}
        with open(os.path.join(os.getcwd(),"data","json", "custom.json"),
                  'w',
                  encoding="utf-8") as file:
            file.write(json.dumps(json_created, indent=4))

    def check_difference_with_config_api(self) -> None:
        """
        Checks if the custom config is different from the config api.
        If it is, the custom config is updated.
        """
        with open(os.path.join(os.getcwd(),"data", "json", "custom.json"),
                  'r',
                  encoding="utf-8") as file1, open(os.path.join(os.getcwd(),
                                                                "data",
                                                                "json",
                                                                "api",
                                                                "config.json"),
                                                   'r',
                                                   encoding="utf-8") as file2:
            custom_config = json.load(file1)["data"]
            config_api = json.load(file2)["data"]

        custom_products = []
        for custom_product_type in custom_config:
            print(custom_product_type["products"])
            custom_products += [{product["name"]: custom_product_type["product_type"]}
                                for product in custom_product_type["products"]]

        config_products = []
        for config_product_type in config_api:
            config_products += [{product["name"]: config_product_type["product_type"]}
                                for product in config_product_type["products"]]

        # Difference between the two lists
        to_add_to_custom = [item for item in config_products if item not in custom_products]

        print(to_add_to_custom)

        self.add_to_custom(config_api, custom_config, to_add_to_custom)

    def add_to_custom(self, config_api, custom_config, to_add_to_custom) -> None:
        """
        Adds to the custom json file the items
        on the api it doesn't have.
        """

        # Adds the product inside custom config to the correct product_type
        if to_add_to_custom:
            for item_not_in_custom in to_add_to_custom:
                item_to_add = {}
                for prod_type in config_api:
                    if prod_type["product_type"] == list(item_not_in_custom.values())[0]:
                        for product in prod_type["products"]:
                            if product["name"] == list(item_not_in_custom.keys())[0]:
                                item_to_add = product
                                break

                for prod_type in custom_config:
                    if item_not_in_custom[
                        list(item_not_in_custom.keys())[0]] == prod_type["product_type"]:
                        prod_type["products"].append(item_to_add)

        with open(os.path.join(os.getcwd(),"data","json", "custom.json"),
                  'w',
                  encoding="utf-8") as file:
            file.write(json.dumps({"data": custom_config}, indent=4))