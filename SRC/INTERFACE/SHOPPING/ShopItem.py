"""
ShopItem.py

Configures the items that can be bought in the shop.
"""

#-------------------------------------------------------------------#

import tkinter as tk

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
        self.container = Container(self.master)
        
        self.container.pack()
        self.name_label = tk.Label(self.container, text=self.name)
        self.amount_label = tk.Label(self.container, text=self.amount)
        
        self.name_label.pack()
        self.amount_label.pack()
        
        for children in self.container.winfo_children():
            children.bind("<Button-1>", self.buy)
               
    def buy(self, event=None):
        """
        Adds one to the amount of the item.
        """
        self.amount += 1
        self.amount_label.configure(text=self.amount) # Actualize the amount label.
        
class Container(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="white")
        