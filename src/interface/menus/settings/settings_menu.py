"""
settings_menu.py

Configure MarcoNeo's settings page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppFrame, AppButton

#-------------------------------------------------------------------#

class SettingsMenu(AppFrame):
    """
    MarcoNeo's settings page.

    Contains the settings of the application such as language, light/dark mode, etc.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

        self.setup_buttons()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the main menu.
        """
        self.language = AppButton(self, text="Language", command=None)
        self.credits_btn = AppButton(self, text="Light/Dark", command=None)
        self.back_btn = AppButton(self, text="Back",
                                  command=lambda: self.gui.change_menu(self.gui.welcome_menu))

        for btn in [self.language, self.credits_btn, self.back_btn]:
            btn.pack()
        return True
