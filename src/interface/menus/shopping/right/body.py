"""
body.py

Configure MarcoNeo's body on its shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame
from src.interface.widgets.shop_item import ShopItem

#-------------------------------------------------------------------#

class Body(Frame):
    """
    Contains the items to be displayed in the shopping page.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager
        self.shopping_manager = manager.manager
        self.grid_propagate(False)
        self.propagate(False)
        self.configure(bg="#333333")
        self.item_per_row = 4

        self.update_body(self.shopping_manager.left_grid.navbar.current_toggle)

    def display_items(self, items):
        """
        Displays the items in the shop.

        Dynamically creates the ShopItem objects.
        """
        row, column = 0, 0
        custom_bool = self.shopping_manager.gui.app.config.name == "custom"
        for item in items:
            if custom_bool:
                if not item["selected"]:
                    continue
            name = item["name"]
            setattr(self, f"{name}_item", ShopItem(name, item["price"], item["id"], self, item["color"]))
            item_frame = getattr(self, f"{name}_item").container
            item_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
            self.grid_columnconfigure(column, weight=1)
            self.grid_rowconfigure(row, weight=1)

            column += 1
            if column == self.item_per_row:
                column = 0
                row += 1

    def update_body(self, toggle):
        """
        Updates the items displayed in the body.
        """
        self.clear_body()
        items_to_display = self.shopping_manager.retrieve_shopping_items(toggle)
        self.display_items(items_to_display)

    def clear_body(self):
        """
        Clears the body.
        """
        for child in self.winfo_children():
            child.destroy()
