"""
MainMenu.py

Configure MarcoNeo's main page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class MainMenu(tk.Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        
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
        tk.Label(self, text="Main menu").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.shopping_btn = tk.Button(self, text="Shopping", command=lambda: self.gui.change_menu(self.gui.shopping_menu))
        self.refill_btn = tk.Button(self, text="Refill", command=lambda: self.gui.change_menu(self.gui.refill_menu))
        self.stats_btn = tk.Button(self, text="Stats", command=lambda: self.gui.change_menu(self.gui.stats_menu))
        self.history_btn = tk.Button(self, text="History", command=lambda: self.gui.change_menu(self.gui.history_menu))
        self.back_btn = tk.Button(self, text="Back", command=lambda: self.gui.change_menu(self.gui.welcome_menu))
        
        
        for btn in [self.shopping_btn, self.refill_btn, self.stats_btn, self.history_btn, self.back_btn]:
            btn.pack()
        