"""
sett_body.py

Body of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame
from src.interface.widgets.sett_item import SettItem

#-------------------------------------------------------------------#

class SettBody(Frame):
    """
    Body of the settings page of the app.
    """
    def __init__(self, manager=None) -> None:
        super().__init__(manager)
        self.settings_manager = manager.manager
        self.propagate(False)
        self.config(bg="#444444")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.item_per_row = 4

        self.update_body(self.settings_manager.left_grid.navbar.current_toggle)

    def display_items(self, items, toggle) -> None:
        """
        Displays the items in the shop.

        Dynamically creates the ShopItem objects.
        """
        row, column = 0, 0
        selected = False
        for item in items:
            name = item["name"]

            # Check if the item is already selected
            for product_type in self.settings_manager.gui.app.config.custom_config:
                if product_type == toggle:
                    for product in product_type["products"]:
                        if product["name"] == name:
                            selected = product["selected"]

            item_frame = SettItem(self, name, selected)
            item_frame.grid(row=row, column=column, padx=30, pady=30, sticky="nsew")
            # Actualise the grid
            self.grid_columnconfigure(column, weight=1)
            self.grid_rowconfigure(row, weight=1)

            column += 1
            if column == self.item_per_row:
                column = 0
                row += 1

    def update_body(self, toggle) -> None:
        """
        Updates the items displayed in the body.
        """
        self.clear_body()
        items_to_display = self.settings_manager.retrieve_settings_items(toggle)
        self.display_items(items_to_display, toggle)

    def clear_body(self) -> None:
        """
        Clears the body.
        """
        for child in self.winfo_children():
            child.destroy()

    def get_selected_items(self) -> list:
        """
        Returns the selected items.
        """
        selected_items = []

        # Add already selected items
        for product_type in self.settings_manager.gui.app.config.custom_config:
            for item in product_type["products"]:
                selected_items.append(item["name"])

        # Add new items
        for child in self.winfo_children():
            if child.selected:
                selected_items.append(child.name)

        selected_items = list(set(selected_items))
        print(selected_items)
        return selected_items
