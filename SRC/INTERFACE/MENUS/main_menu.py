"""
MainMenu.py

Configure MarcoNeo's main page.
"""

#-------------------------------------------------------------------#

from SRC.utils.gui_utils import Frame, Label, AppButton

#-------------------------------------------------------------------#

class MainMenu(Frame):
    """
    MarcoNeo's main page.

    It contains the main actions of the application such
    as shopping, stats, history, etc.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

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
        self.stats_btn = AppButton(self, text="Stats",
                                   command=lambda: self.gui.change_menu(self.gui.stats_menu))
        self.history_btn = AppButton(self, text="History",
                                     command=lambda: self.gui.change_menu(self.gui.history_menu))
        self.back_btn = AppButton(self, text="Back",
                                  command=lambda: self.gui.change_menu(self.gui.welcome_menu))


        for btn in [self.shopping_btn, self.stats_btn, self.history_btn, self.back_btn]:
            btn.pack()
        return True
