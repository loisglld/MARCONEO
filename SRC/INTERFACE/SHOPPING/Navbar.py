"""
Nabar.py

Configure MarcoNeo's navbar on its shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.tkinter_utils import Frame, Label, Button

#-------------------------------------------------------------------#

class Navbar(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="black")
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
        Label(self, text="Navbar").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.lunch_btn = Button(self, text="Lunch", command=None)
        self.snack_btn = Button(self, text="Snack", command=None)
        self.party_btn = Button(self, text="Party", command=None)
        self.refill_btn = Button(self, text="Refill", command=None)
        self.back_btn = Button(self, text="Back", command=lambda: self.master.gui.change_menu(self.master.gui.main_menu))
        
        for btn in [self.lunch_btn, self.snack_btn, self.party_btn, self.refill_btn, self.back_btn]:
            btn.pack()