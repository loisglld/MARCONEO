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

        self.change_config_btn = AppButton(self, text="Change config",
                                    command=self.change_config)


        self.change_config_btn.pack(side="top", pady=10, padx=10, fill="x")
        self.back_btn.pack(side="bottom", pady=10, padx=10, fill="x")

    def change_config(self) -> None:
        """
        Changes the menu to the main menu.
        """
        # Generate a new config file

        # Change the current config file loaded
        self.manager.manager.gui.app.config.load("config")

        # Actualise the welcome menu
        self.manager.manager.gui.welcome_menu.config_loaded_lbl.config(text="Config loaded: config")
