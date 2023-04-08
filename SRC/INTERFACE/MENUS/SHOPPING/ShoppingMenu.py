"""
ShoppingMenu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.MENUS.SHOPPING.LEFT.LeftGrid import LeftGrid
from SRC.INTERFACE.MENUS.SHOPPING.RIGHT.RightGrid import RightGrid
from SRC.INTERFACE.gui_utils import Frame

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        self.current_toggle = "Lunch"
        
        # Setup the left grid for the navbar
        self.left_grid = LeftGrid(self)
        self.left_grid.grid(row=0, column=0, sticky='nsew')
        
        # Setup the right grid for the header, body and footer
        self.right_grid = RightGrid(self)
        self.right_grid.grid(row=0, column=1, sticky='nsew')

        
    def retrieve_shopping_items(self, toggle:str):
        """
        Retrieves the items to display.
        """
        items = self.gui.app.config['Shopping'][toggle]['items']
        return items
                