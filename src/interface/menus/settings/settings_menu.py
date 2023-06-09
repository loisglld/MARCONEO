"""
settings_menu.py

Configure MarcoNeo's settings page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppFrame
from src.interface.menus.settings.left.left_sett import LeftSett
from src.interface.menus.settings.right.right_sett import RightSett

#-------------------------------------------------------------------#

class SettingsMenu(AppFrame):
    """
    MarcoNeo's settings page.

    Contains the settings of the application:
    Fouaille will be able to config the items
    they want to see in the shopping menu.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui
        self.propagate(False)

        # Setup the left grid for the navbar
        self.left_grid = LeftSett(self)
        self.left_grid.grid(row=0, column=0, sticky="nsew")

        # Setup the right grid for the header, body and footer
        self.right_grid = RightSett(self)
        self.right_grid.grid(row=0, column=1, sticky="nsew")

        # Setup the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

    def retrieve_settings_items(self, toggle):
        """
        Retrieves from api_config.json the items
        following the toggle.
        """
        data = self.gui.app.config.api_config.config_json
        items = []
        for menu in data:
            if menu["product_type"] == toggle:
                items = menu["products"]
                break
        return items

    def refresh(self):
        """
        Refreshes the settings page.
        """
        self.gui.app.config.api_config.setup_jsons()
        self.right_grid.body.update_body(self.left_grid.navbar.current_toggle)

    def save(self) -> None:
        """
        Saves the settings page's selections to the custom json file.
        """
        custom_data = []
        custom_items_list = self.right_grid.body.get_selected_items()
        for item_names in custom_items_list:
            for item in self.gui.app.config.api_config.config_json:
                for product in item["products"]:
                    if product["name"] == item_names:
                        # Vérifier si le type de produit existe déjà dans custom_data
                        product_type_exists = False
                        for custom_item in custom_data:
                            if custom_item["product_type"] == item["product_type"]:
                                custom_item["products"].append(product)
                                product_type_exists = True
                                break
                        if not product_type_exists:
                            custom_item = {
                                "id": item["id"],
                                "product_type": item["product_type"],
                                "products": [product]
                            }
                            custom_data.append(custom_item)

        self.gui.app.config.update_custom_file(custom_data)
