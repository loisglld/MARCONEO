"""
graphic_user_interface.py

This script describes the GUI class.
It is responsible for the GUI of the BT application.
"""

#------------------------------------------------------------#

from SRC.utils.gui_utils import Tk, Frame, BOTH

from SRC.INTERFACE.MENUS.welcome_menu import WelcomeMenu
from SRC.INTERFACE.MENUS.credits_menu import CreditsMenu
from SRC.INTERFACE.MENUS.SETTINGS.settings_menu import SettingsMenu
from SRC.INTERFACE.MENUS.main_menu import MainMenu
from SRC.INTERFACE.MENUS.SHOPPING.ShoppingMenu import ShoppingMenu

from SRC.utils.decorators import close_service, launch_service

#------------------------------------------------------------#

class GUI(Tk):
    """
    Graphic User Interface of the application.
    """
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.loggers = self.app.loggers
        self.current_menu = None

        self.bind("<Key>", self.app.rfid.rfid_callback) # Listen to the RFID reader
        self.loggers.log.debug("RFID is listening.")

        self.setup_window()
        self.setup_menus()

    def change_menu(self, next_menu: Frame):
        """
        This function changes the current view to the desired menu.
        """
        # Don't do anything if the desired menu is the same as the current menu
        if next_menu == self.current_menu:
            return

        # Unbind the keyboard
        self.unbind("<Key>")

        self.current_menu.pack_forget()
        next_menu.pack(fill=BOTH, expand=True)
        # Update the current menu reference
        self.current_menu = next_menu
        self.loggers.log.debug(f"({type(next_menu).__name__})")

        # Re-bind the keyboard
        self.bind("<Key>", self.app.rfid.rfid_callback)

    @launch_service
    def setup_window(self):
        """
        Setup the window of the application.
        """
        self.title("MarcoNeo")
        self.geometry("800x480")
        self.resizable(False, False)
        #self.iconbitmap(os.path.join(os.getcwd(),"DATA","IMAGES","logo.ico"))
        #self.config(bg="black")

    def setup_menus(self):
        """
        Setup the different menus of the application.
        """
        self.welcome_menu = WelcomeMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.settings_menu = SettingsMenu(self)
        self.main_menu = MainMenu(self)

        self.shopping_menu = ShoppingMenu(self)
        self.history_menu = Frame(self)
        self.stats_menu = Frame(self)

        self.welcome_menu.pack(fill=BOTH, expand=True)
        self.current_menu = self.welcome_menu

    def start(self):
        """
        Displays the GUI.
        """
        self.mainloop()

    @close_service
    def close(self):
        """
        This function is called when the user closes the application.
        """
        self.quit()
        self.loggers.log.debug("GUI closed.")
        return True
