"""
MainMenu.py

Configure MarcoNeo's main page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class MainMenu(tk.Frame):
    def __init__(self, app=None):
        super().__init__(app)
        self.app = app
        self.app.loggers.log.info("(Main menu)")
        
        self.setup_images()
        self.setup_label()
        self.setup_buttons()
        
    def setup_images(self):
        """
        Defines the images used in the main menu.
        """
        return
    
    def setup_label(self):
        """
        Defines the labels used in the main menu.
        """
        return
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        return
        