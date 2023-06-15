"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

import decimal
from src.utils.gui_utils import AppLabel, Frame, Label

#-------------------------------------------------------------------#

class ShopItem(Frame):
    """
    Describes an item that can be bought in the shop.
    """
    def __init__(self, title:str, price, id_product, manager=None, color:str="#555555",
                 width:int=120, height:int=120):
        """
        Item's constructor.
        """
        super().__init__(manager)
        self.configure(bg="black", width=width, height=height)
        self.color = color
        self.manager = manager
        self.gui_manager = self.manager.manager.manager.gui
        self.cart = self.gui_manager.app.cart
        self.footer = self.manager.manager.footer

        # Background image
        img = getattr(self.gui_manager, f"img_{title.lower().replace(' ', '')}")
        self.bg_lbl = Label(self, image=img,
                            borderwidth=0, highlightthickness=0)
        # We use place so that the image is in the background
        self.bg_lbl.place(x=0, y=0)

        self.title = title.title()
        self.id_product = id_product
        self.price = decimal.Decimal(price)
        self.amount = 0

        self.name_label = None
        self.amount_label = None
        self.price_label = None

        self.setup_container()

    def setup_container(self):
        """
        Defines the container of the item.
        """
        # The name and the amount are labels inside the Frame.
        self.name_label = AppLabel(self, text=self.title,
                                   bg=self.color, font=("system", 15))
        self.amount_label = AppLabel(self, text=self.amount,
                                     bg=self.color, font=("system", 15))
        self.price_label = AppLabel(self, text=str(self.price)+"€",
                                    bg=self.color, font=("system", 15))

        self.name_label.place(relx=0.5, rely=0.2, anchor="center")
        self.amount_label.place(relx=0.5, rely=0.5, anchor="center")
        self.price_label.place(relx=0.5, rely=0.8, anchor="center")

        # Binds to the whole widget
        self.bind("<Button-1>", self.add_item)
        for children in self.winfo_children():
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
        return self.title
