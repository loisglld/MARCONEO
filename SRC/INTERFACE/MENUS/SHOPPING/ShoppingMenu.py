"""
ShoppingMenu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.MENUS.SHOPPING.Navbar import Navbar
from SRC.INTERFACE.MENUS.SHOPPING.Header import Header
from SRC.INTERFACE.MENUS.SHOPPING.Body import Body
from SRC.INTERFACE.MENUS.SHOPPING.Footer import Footer
from SRC.INTERFACE.gui_utils import Frame

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        self.current_toggle = "Lunch"
        
        # Setup the left grid for the navbar
        self.left_grid = Frame(self)
        self.left_grid.grid(row=0, column=0, sticky='nsew')

        # Setup the navbar inside the left grid
        self.navbar = Navbar(self.left_grid)
        self.navbar.grid(row=0, column=0, sticky='nsew')

        # Setup the right grid for the header, body and footer
        self.right_grid = Frame(self)
        self.right_grid.grid(row=0, column=1, sticky='nsew')

        # Setup the header inside the right grid
        self.header = Header(self.right_grid)
        self.header.grid(row=0, column=0, sticky='nsew')

        # Setup the body inside the right grid
        self.body = Body(self.right_grid)
        self.body.grid(row=1, column=0, sticky='nsew')

        # Setup the footer inside the right grid
        self.footer = Footer(self.right_grid)
        self.footer.grid(row=2, column=0, sticky='nsew')

        # Setup proportions for the left grid
        self.left_grid.grid_rowconfigure(0, weight=1)

        # Setup proportions for the right grid
        self.right_grid.grid_rowconfigure(0, weight=1)
        self.right_grid.grid_rowconfigure(1, weight=8)
        self.right_grid.grid_rowconfigure(2, weight=1)
        self.right_grid.grid_columnconfigure(0, weight=1)

        
    def retrieve_shopping_items(self, toggle:str):
        """
        Retrieves the items to display.
        """
        items = self.gui.app.config['Shopping'][toggle]['items']
        return items
                