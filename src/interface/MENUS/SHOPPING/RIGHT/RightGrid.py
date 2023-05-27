"""
RightGrid.py

Container of the header, body and footer of the shopping page.
"""

#-------------------------------------------------------------------#

from src.interface.MENUS.SHOPPING.RIGHT.Header import Header
from src.interface.MENUS.SHOPPING.RIGHT.Body import Body
from src.interface.MENUS.SHOPPING.RIGHT.Footer import Footer
from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#


class RightGrid(Frame):
    """
    Container of the header, body and footer of the shopping page.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager

        self.grid_propagate(False)

        # Setup the header inside the right grid
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky='nsew')

        # Setup the footer inside the right grid
        self.footer = Footer(self)
        self.footer.grid(row=2, column=0, sticky='nsew')

        # Setup the body inside the right grid
        self.body = Body(self)
        self.body.grid(row=1, column=0, sticky='nsew')

        # Setup the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=2)

