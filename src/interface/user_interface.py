"""
graphic_user_interface.py

This script describes the GUI class.
It is responsible for the GUI of the MarcoNeo application.
"""

#------------------------------------------------------------#

from src.utils.gui_utils import Tk, Frame, BOTH

from src.interface.menus.welcome_menu import WelcomeMenu
from src.interface.menus.credits_menu import CreditsMenu
from src.interface.menus.settings.settings_menu import SettingsMenu
from src.interface.menus.history.history_menu import HistoryMenu
from src.interface.menus.main_menu import MainMenu
from src.interface.menus.shopping.shopping_menu import ShoppingMenu

#------------------------------------------------------------#

class GUI(Tk):
    """
    Graphical User Interface of the application.
    """
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.loggers = self.app.loggers
        self.protocol("WM_DELETE_WINDOW", self.app.close)
        self.main_menu = None
        self.shopping_menu = None
        self.history_menu = None
        self.stats_menu = None

        self.bind("<Key>", self.app.rfid.rfid_callback) # Listen to the RFID reader
        self.loggers.log.debug("RFID is listening.")

        self.setup_window()
        self.welcome_menu = WelcomeMenu(self)
        self.settings_menu = SettingsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.welcome_menu.pack(fill=BOTH, expand=True)
        self.current_menu = self.welcome_menu

    def change_menu(self, next_menu: Frame) -> None:
        """
        This function changes the current view to the desired menu.
        """
        # Don't do anything if the desired menu is the same as the current menu
        if next_menu == self.current_menu:
            return

        # Unbind the keyboard
        self.unbind("<Key>")

        next_menu.pack(fill=BOTH, expand=True)

        # Check night mode

        self.current_menu.pack_forget()

        # Re-bind the keyboard
        self.bind("<Key>", self.app.rfid.rfid_callback)

        # Update the current menu reference
        self.current_menu = next_menu
        self.loggers.log.debug(f"({type(next_menu).__name__})")

    def setup_window(self) -> bool:
        """
        Setup the window of the application.
        """
        self.title("MarcoNeo")
        self.geometry("800x480")
        self.resizable(False, False)
        #self.iconbitmap(os.path.join(os.getcwd(),"DATA","IMAGES","logo.ico"))
        #self.config(bg="black")
        return True

    def setup_menus(self) -> bool:
        """
        Setup the different menus of the application.
        These menus need a config to be loaded.
        """
        self.main_menu = MainMenu(self)
        self.shopping_menu = ShoppingMenu(self)
        self.history_menu = HistoryMenu(self)
        return True

    def start(self) -> bool:
        """
        Displays the GUI.
        """
        self.mainloop()
        return True

    def close(self) -> bool:
        """
        This function is called when the user closes the application.
        """
        self.quit()
        self.loggers.log.debug("GUI closed.")
        return True
