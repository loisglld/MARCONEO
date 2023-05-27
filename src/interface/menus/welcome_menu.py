"""
welcome_menu.py

Configure MarcoNeo's welcome page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Label, AppButton, AppFrame

#-------------------------------------------------------------------#

class WelcomeMenu(AppFrame):
    """
    MarcoNeo's welcome page.

    It is the first page to appear
    when the application is launched.
    """
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui

        self.setup_label()
        self.setup_buttons()

    def setup_label(self):
        """
        Defines the labels used in the main menu.
        """
        Label(self, text="Welcome to MarcoNeo").pack()

    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.enter_btn = AppButton(self, text="Enter",
                                   command=lambda: self.gui.change_menu(self.gui.main_menu))
        self.settings_btn = AppButton(self, text="Settings",
                                      command=lambda: self.gui.change_menu(self.gui.settings_menu))
        self.credits_btn = AppButton(self, text="Credits",
                                     command=lambda: self.gui.change_menu(self.gui.credits_menu))
        self.power_btn = AppButton(self, text="Power off",
                                   command=self.gui.app.close)

        for btn in [self.enter_btn, self.settings_btn, self.credits_btn, self.power_btn]:
            btn.pack()
