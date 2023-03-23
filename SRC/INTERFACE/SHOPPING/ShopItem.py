"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class ShopItem:
    def __init__(self, name, master=None):
        """
        Item's constructor.
        """
        self.master = master
        self.name = name
        self.amount = 0
        self.setup_container()
        
    def setup_container(self):
        """
        Defines the container of the item.
        """
        # The container is a Frame.
        self.container = Frame(self.master)
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
        """
        self.amount += 1
        self.master.master.gui.app.current_user.cart.add_to_cart(self)
        self.master.master.footer.update_total_label()
        self.amount_label.configure(text=self.amount) # Actualize the amount label.
        self.master.master.footer.update_total_label() # Actualize the total label.
    