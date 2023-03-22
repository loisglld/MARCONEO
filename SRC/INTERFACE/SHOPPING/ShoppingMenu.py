"""
ShoppingMenu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.SHOPPING.Navbar import Navbar
from SRC.INTERFACE.SHOPPING.Body import Body
from SRC.INTERFACE.gui_utils import Frame

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        self.current_toggle = "Lunch"
        
        # Setup the body
        self.body = Body(self)
        self.body.grid(row=0, column=1, sticky='nsew')
        
        # Setup the navbar
        self.navbar = Navbar(self)
        self.navbar.grid(row=0, column=0, rowspan=2, sticky='nsew')
        
        # Setup proportions
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(0, weight=1)
        
    def retrieve_shopping_items(self, toggle:str):
        """
        Retrieves the items to display.
        """
        items = self.gui.app.config['Shopping'][toggle]['items']
        return items
                