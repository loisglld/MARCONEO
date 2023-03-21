"""
MainMenu.py

Configure MarcoNeo's main page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.tkinter_utils import Frame, Label, Button

#-------------------------------------------------------------------#

class MainMenu(Frame):
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
        Label(self, text="Main menu").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.shopping_btn = Button(self, text="Shopping", command=lambda: self.gui.change_menu(self.gui.shopping_menu))
        self.stats_btn = Button(self, text="Stats", command=lambda: self.gui.change_menu(self.gui.stats_menu))
        self.history_btn = Button(self, text="History", command=lambda: self.gui.change_menu(self.gui.history_menu))
        self.back_btn = Button(self, text="Back", command=lambda: self.gui.change_menu(self.gui.welcome_menu))
        
        
        for btn in [self.shopping_btn, self.stats_btn, self.history_btn, self.back_btn]:
            btn.pack()
        