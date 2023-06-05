"""
body.py

Configure MarcoNeo's body on its shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label
from src.interface.menus.shopping.shop_item import ShopItem

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
        self.configure(bg="#333333")
        # Bind the security after the __init__ of body
        self.shopping_manager.left_grid.navbar.refill_btn.config(command=self.refill_security)

        self.item_per_row = 3

        self.update_body(self.shopping_manager.left_grid.navbar.current_toggle)

    def display_items(self, items):
        """
        Displays the items in the shop.

        Dynamically creates the ShopItem objects.
        """
        row, column = 0, 0
        for item in items:
            name = item["name"]
            price = item["price"]
            setattr(self, f"{name}_item", ShopItem(name, price, self))
            item_frame = getattr(self, f"{name}_item").container
            item_frame.grid(row=row, column=column, padx=10, pady=10)
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

    def refill_security(self):
        """
        If the curretn user isn't an admin,
        then an error message is displayed and,
        asks the user to scan an admin card.
        """
        self.clear_body()
        if self.shopping_manager.gui.app.current_user.is_admin:
            self.shopping_manager.left_grid.navbar.current_toggle = "Refill"
            self.shopping_manager.left_grid.navbar.toggle("Refill")
            self.update_body(self.shopping_manager.left_grid.navbar.current_toggle)
            return
        Label(self, text="""To refill you need to be an admin.
        Please scan an admin card and click again on refill.

        Only next, you will be able to refill any other card.""",
        bg="#333333", fg="white").pack()
