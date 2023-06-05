"""
shopping_menu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from src.interface.menus.shopping.left.left_grid import LeftGrid
from src.interface.menus.shopping.right.right_grid import RightGrid
from src.utils.gui_utils import Frame
from src.interface.menus.shopping.right.price_modifier import PriceModifier

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    """
    Menu for the shopping page.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

        # Setup the left grid for the navbar
        self.left_grid = LeftGrid(self)
        self.left_grid.grid(row=0, column=0, sticky='nsew')

        # Setup the right grid for the header, body and footer
        self.right_grid = RightGrid(self)
        self.right_grid.grid(row=0, column=1, sticky='nsew')

        # Setup the price modifier
        self.price_modifier = PriceModifier(self.right_grid)

        # Setup the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

    def retrieve_shopping_items(self, toggle:str) -> list:
        """
        Retrieves the items to display.
        """
        items = self.gui.app.config['Shopping'][toggle]['items']
        return items

    def modify_prices(self):
        """
        Opens the price modifier.
        """
        self.price_modifier.pack(side="top", fill="both", expand=True)
        self.right_grid.header.grid_forget()
        self.right_grid.body.grid_forget()
        self.right_grid.footer.grid_forget()
