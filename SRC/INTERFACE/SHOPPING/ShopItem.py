"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.tkinter_utils import Frame, Label

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
        self.container = Frame(self.master)
        self.container.configure(bg="white")
        self.container.pack()
        
        self.name_label = Label(self.container, text=self.name)
        self.amount_label = Label(self.container, text=self.amount)
        
        self.name_label.pack()
        self.amount_label.pack()
        
        self.container.bind("<Button-1>", self.buy)
        for children in self.container.winfo_children():
            children.bind("<Button-1>", self.buy)
               
    def buy(self, event=None):
        """
        Adds one to the amount of the item.
        """
        self.amount += 1
        self.amount_label.configure(text=self.amount) # Actualize the amount label.
        