"""
GUI.py

This script describes the GUI class.
It is responsible for the GUI of the BT application.
"""

#------------------------------------------------------------#

from SRC.INTERFACE.MainMenu import MainMenu
from SRC.INTERFACE.RFID import RFID

import tkinter as tk
import os

#------------------------------------------------------------#

class GUI(tk.Tk):
    def __init__(self, loggers):
        super().__init__()
        self.loggers = loggers
        
        self.rfid = RFID(self.loggers)
        self.bind("<Key>", self.rfid.rfid_callback) # Listen to the RFID reader
        
        self.setup_window()
        self.setup_menus()
        
    def change_menu(self, next_menu: tk.Frame):
        """
        This function changes the current view to the desired menu.
        """
        # Don't do anything if the desired menu is the same as the current menu
        if next_menu == self.current_menu:
            return

        self.current_menu.pack_forget()
        next_menu.pack(fill=tk.BOTH, expand=True)
        # Update the current menu reference
        self.current_menu = next_menu
    
    def setup_window(self):
        """
        Setup the window of the application.
        """
        self.title("MarcoNeo")
        self.geometry("800x480")
        self.resizable(False, False)
        self.iconbitmap(os.path.join(os.getcwd(),"DATA","IMAGES","logo.ico"))
                
    def setup_menus(self):
        """
        Setup the different menus of the application.
        """
        self.main_menu = MainMenu(self)
        """self.credits_menu = CreditsMenu(self)
        self.settings_menu = SettingsMenu(self)
        
        self.game_menu = GameMenu(self)"""
        
        #self.main_menu.pack(fill=tk.BOTH, expand=True)
        self.current_menu = self.main_menu
        
    def start(self):
        """
        Displays the GUI.
        """
        self.mainloop()
        
    def close(self):
        """
        This function is called when the user closes the application.
        """
        self.quit()
        self.loggers.log.debug("GUI closed.")