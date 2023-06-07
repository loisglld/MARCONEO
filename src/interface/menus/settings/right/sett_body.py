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
        self.config(bg="blue")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.item_per_row = 4

        self.update_body(self.settings_manager.left_grid.navbar.current_toggle)

    def display_items(self, items):
        """
        Displays the items in the shop.

        Dynamically creates the ShopItem objects.
        """
        row, column = 0, 0
        for item in items:
            name = item["name"]
            setattr(self, f"{name}_item", SettItem(self, name))
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
        items_to_display = self.settings_manager.retrieve_settings_items(toggle)
        self.display_items(items_to_display)

    def clear_body(self):
        """
        Clears the body.
        """
        for child in self.winfo_children():
            child.destroy()
