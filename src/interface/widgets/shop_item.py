"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

import decimal
from src.utils.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class ShopItem:
    """
    Describes an item that can be bought in the shop.
    """
    def __init__(self, name, price, id_product, manager=None, color:str="#333333"):
        """
        Item's constructor.
        """
        self.color = color
        self.manager = manager
        self.cart = self.manager.manager.manager.gui.app.cart
        self.footer = self.manager.manager.footer

        # The container is a Frame.
        self.container = Frame(self.manager)
        self.container.configure(bg=self.color)
        self.container.propagate(False)

        self.name = name
        self.id_product = id_product
        self.price = decimal.Decimal(price)
        self.amount = 0

        self.setup_container()

    def setup_container(self):
        """
        Defines the container of the item.
        """

        # The name and the amount are labels inside the Frame.
        self.name_label = Label(self.container, text=self.name)
        self.amount_label = Label(self.container, text=self.amount)
        self.price_label = Label(self.container, text=str(self.price)+"€")

        self.name_label.pack(side="top", padx=10, pady=5, fill="both", expand=True)
        self.amount_label.pack(side="top", padx=10, pady=5, fill="both", expand=True)
        self.price_label.pack(side="top", padx=10, pady=5, fill="both", expand=True)

        # Binds to the whole widget
        self.container.bind("<Button-1>", self.add_item)
        for children in self.container.winfo_children():
            children.bind("<Button-1>", self.add_item)

    def add_item(self, _event=None):
        """
        Adds one to the amount of the item.
        The amount is increased by one inside the body of ShoppingMenu.
        The item is added to the cart. The footer's total label is actualized.
        """
        if self.manager.manager.manager.gui.app.current_user.card_id is None:
            return

        # Cart's modification
        self.amount += 1
        self.cart.add_to_cart({self.id_product: (self.amount, self.price)})
        self.cart.total += self.price

        # Body's modification
        self.amount_label.configure(text=self.amount)

        # Footer's modification
        self.footer.update_footer()

    def __repr__(self) -> str:
        return self.name
