"""
LeftGrid.py

Container of the navbar of the shopping page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.MENUS.SHOPPING.LEFT.Navbar import Navbar
from SRC.INTERFACE.gui_utils import Frame

#-------------------------------------------------------------------#


class LeftGrid(Frame):
    def __init__(self):
        self.navbar = Navbar(self.left_grid)
        self.navbar.pack()
