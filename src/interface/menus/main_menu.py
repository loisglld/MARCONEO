"""
MainMenu.py

Configure MarcoNeo's main page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppFrame, Label, AppButton

#-------------------------------------------------------------------#

class MainMenu(AppFrame):
    """
    MarcoNeo's main page.

    It contains the main actions of the application such
    as shopping, stats, history, etc.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui
        if self.gui.app.config is None:
            self.gui.app.loggers.log.warn("There is no config file loaded.")
            return

        self.setup_images()
        self.setup_label()
        self.setup_buttons()

    def setup_images(self) -> None:
        """
        Defines the images used in the main menu.
        """
        return

    def setup_label(self) -> None:
        """
        Defines the labels used in the main menu.
        """
        Label(self, text="Main menu").pack()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the main menu.
        """
        self.shopping_btn = AppButton(self, text="Shopping",
                                      command=lambda: self.gui.change_menu(self.gui.shopping_menu))
        self.history_btn = AppButton(self, text="History",
                                     command=self.history)
        self.back_btn = AppButton(self, text="Back",
                                  command=lambda: self.gui.change_menu(self.gui.welcome_menu))

        for btn in [self.shopping_btn, self.history_btn]:
            btn.pack(side="top", pady=10, padx=10, fill="x")

        self.back_btn.pack(side="bottom", pady=10, padx=10, fill="x")
        return True

    def history(self) -> True:
        """
        Change menu to history menu.
        """
        self.gui.history_menu.refresh_history()
        self.gui.change_menu(self.gui.history_menu)
        return True
