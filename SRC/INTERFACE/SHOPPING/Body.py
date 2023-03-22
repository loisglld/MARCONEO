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
        self.master = master
        self.grid_propagate(False)
        self.configure(bg="#333333")
        self.item_per_row = 3
        
        self.update_body(self.master.current_toggle)
           
    def display_items(self, items):
        """
        Displays the items in the shop.
        """
        row, column = 0, 0
        for i, item in enumerate(items):
            name = item["name"]
            setattr(self, f"{name}_item", ShopItem(name, self))
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
        items_to_display = self.master.retrieve_shopping_items(toggle)
        self.display_items(items_to_display)
        
    def clear_body(self):
        """
        Clears the body.
        """
        for child in self.winfo_children():
            child.destroy()
                