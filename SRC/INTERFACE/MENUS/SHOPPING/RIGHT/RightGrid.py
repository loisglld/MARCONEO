"""
RightGrid.py

Container of the header, body and footer of the shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.MENUS.SHOPPING.RIGHT.Header import Header
from SRC.INTERFACE.MENUS.SHOPPING.RIGHT.Body import Body
from SRC.INTERFACE.MENUS.SHOPPING.RIGHT.Footer import Footer
from SRC.INTERFACE.gui_utils import Frame

#-------------------------------------------------------------------#


class RightGrid(Frame):
    def __init__(self, master=None):
        self.master = master
        
        # Setup the header inside the right grid
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky='nsew')

        # Setup the body inside the right grid
        self.body = Body(self)
        self.body.grid(row=1, column=0, sticky='nsew')

        # Setup the footer inside the right grid
        self.footer = Footer(self)
        self.footer.grid(row=2, column=0, sticky='nsew')
