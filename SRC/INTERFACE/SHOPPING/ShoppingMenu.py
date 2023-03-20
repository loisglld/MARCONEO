"""
ShoppingMenu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.SHOPPING.Navbar import Navbar
from SRC.INTERFACE.SHOPPING.Body import Body
from SRC.INTERFACE.tkinter_utils import Frame

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        self.body = Body(self)
        self.body.grid(row=0, column=1, sticky='nsew')
        
        self.navbar = Navbar(self)
        self.navbar.grid(row=0, column=0, rowspan=2, sticky='nsew')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(0, weight=1)
        