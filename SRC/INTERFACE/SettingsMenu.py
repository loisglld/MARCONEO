"""
SettingsMenu.py.py

Configure MarcoNeo's settings page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class SettingsMenu(tk.Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        #self.gui.loggers.log.debug("(Main menu)")
        
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
        tk.Label(self, text="Settings menu").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.language = tk.Button(self, text="Language", command=None)
        self.credits_btn = tk.Button(self, text="Light/Dark", command=None)
        self.back_btn = tk.Button(self, text="Back", command=lambda: self.gui.change_menu(self.gui.main_menu))
                
        for btn in [self.language, self.credits_btn, self.back_btn]:
            btn.pack()
        