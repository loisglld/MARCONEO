"""
Body.py

Configure MarcoNeo's body on its shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.tkinter_utils import Frame
from SRC.INTERFACE.SHOPPING.ShopItem import ShopItem

#-------------------------------------------------------------------#

class Body(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="#333333")
        self.setup_items()
        
    def setup_items(self):
        """
        Defines the items that can be bought in the shop.
        """
        self.item1 = ShopItem("Item 1", self)
        self.item2 = ShopItem("Item 2", self)
        self.item3 = ShopItem("Item 3", self)
        """self.items = []
        for item in dir(self):
            if type(item) == type(ShopItem):
                self.items.append(item)
                
        print(self.items)"""
        
    def display_items(self):
        """
        Displays the items in the shop.
        """
        for item in self.items:
            item.pack()