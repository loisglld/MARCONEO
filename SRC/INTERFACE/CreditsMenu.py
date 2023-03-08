"""
CreditsMenu.py.py

Configure MarcoNeo's credits page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class CreditsMenu(tk.Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        #self.gui.loggers.log.debug("(Credits menu)")
        
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
        tk.Label(self, text="Credits menu").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.back_btn = tk.Button(self, text="Back", command=lambda: self.gui.change_menu(self.gui.welcome_menu))
        
        self.back_btn.pack()