"""
LeftGrid.py

Container of the navbar of the shopping page.
"""

#-------------------------------------------------------------------#

from src.interface.menu_templates.navbar import Navbar
from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#


class LeftGrid(Frame):
    """
    Container of the navbar of the shopping page.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager

        self.propagate(False)

        self.navbar = Navbar(self)
        self.navbar.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
