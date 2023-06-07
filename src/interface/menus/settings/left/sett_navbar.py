"""
sett_navbar.py

Navbar of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton

#-------------------------------------------------------------------#

class SettNavbar(Frame):
    """
    Navbar of the settings page of the app.
    """
    def __init__(self, left_grid=None):
        super().__init__(left_grid)
        self.manager = left_grid
        self.config(bg="#000000")
        self.back_btn = None
        self.setup_buttons()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the navbar.
        """
        self.back_btn = AppButton(self, text="Back",
                                    command=lambda:
                                        self.manager.manager.gui.change_menu(
                                            self.manager.manager.gui.welcome_menu))

        self.back_btn.pack(side="bottom", pady=10, padx=10, fill="x")
