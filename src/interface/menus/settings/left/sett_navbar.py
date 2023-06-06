"""
sett_navbar.py

Navbar of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#

class SettNavbar(Frame):
    """
    Navbar of the settings page of the app.
    """
    def __init__(self, left_grid=None):
        super().__init__(left_grid)
        self.manager = left_grid
        self.config(bg="#000000")
