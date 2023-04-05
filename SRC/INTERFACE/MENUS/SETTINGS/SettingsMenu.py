"""
SettingsMenu.py.py

Configure MarcoNeo's settings page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label, AppButton

#-------------------------------------------------------------------#

class SettingsMenu(Frame):
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
        Label(self, text="Settings menu").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.language = AppButton(self, text="Language", command=None)
        self.credits_btn = AppButton(self, text="Light/Dark", command=None)
        self.back_btn = AppButton(self, text="Back", command=lambda: self.gui.change_menu(self.gui.welcome_menu))
                
        for btn in [self.language, self.credits_btn, self.back_btn]:
            btn.pack()
        