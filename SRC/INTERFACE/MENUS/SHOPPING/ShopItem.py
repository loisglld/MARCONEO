"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class ShopItem:
    def __init__(self, name, price, master=None):
        """
        Item's constructor.
        """
        self.body_master = master
        self.cart = self.body_master.master.gui.app.cart
        self.footer = self.body_master.shopping_master.footer
        
        self.name = name
        self.price = price
        self.amount = 0
        
        self.setup_container()
        
    def setup_container(self):
        """
        Defines the container of the item.
        """
        # The container is a Frame.
        self.container = Frame(self.body_master)
        self.container.configure(bg="white")
        
        # The name and the amount are labels inside the Frame.
        self.name_label = Label(self.container, text=self.name)
        self.amount_label = Label(self.container, text=self.amount)
        
        self.name_label.pack()
        self.amount_label.pack()
        
        self.container.bind("<Button-1>", self.add_item)
        for children in self.container.winfo_children():
            children.bind("<Button-1>", self.add_item)
               
    def add_item(self, event=None):
        """
        Adds one to the amount of the item.
        The amount is increased by one inside the body of ShoppingMenu.
        The item is added to the cart. The footer's total label is actualized.       
        """
        # Self's modification
        self.amount += 1
        
        # Body's modification
        self.amount_label.configure(text=self.amount)
        
        # Cart's modification
        if not self in self.cart.items: self.cart.add_to_cart(self)
        self.cart.total += self.price
    
        # Footer's modification
        self.footer.update_footer()
        
    def __str__(self) -> str:
        return f"{self.name} x{self.amount}"
