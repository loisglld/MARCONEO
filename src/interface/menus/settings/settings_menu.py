"""
settings_menu.py

Configure MarcoNeo's settings page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppFrame
from src.interface.menus.settings.left.left_sett import LeftSett
from src.interface.menus.settings.right.right_sett import RightSett

#-------------------------------------------------------------------#

class SettingsMenu(AppFrame):
    """
    MarcoNeo's settings page.

    Contains the settings of the application such as language, light/dark mode, etc.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

        # Setup the left grid for the navbar
        self.left_grid = LeftSett(self)
        self.left_grid.pack(side="left", fill="both", expand=True)

        # Setup the right grid for the header, body and footer
        self.right_grid = RightSett(self)
        self.right_grid.pack(side="right", fill="both", expand=True)

        # Setup the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
