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
        self.lunch_btn = Button(self, text="Lunch", command=lambda: self.toggle("Lunch"))
        self.snack_btn = Button(self, text="Snack", command=lambda: self.toggle("Snack"))
        self.shots_btn = Button(self, text="Shots", command=lambda: self.toggle("Shots"))
        self.oeno_btn = Button(self, text="Oeno", command=lambda: self.toggle("Oeno"))
        self.party_btn = Button(self, text="Party", command=lambda: self.toggle("Party"))
        self.refill_btn = Button(self, text="Refill", command=lambda: self.toggle("Refill"))
        self.back_btn = Button(self, text="Back", command=lambda: self.master.gui.change_menu(self.master.gui.main_menu))
        
        for btn in [self.lunch_btn, self.snack_btn, self.party_btn, self.refill_btn, self.back_btn]:
            btn.pack()
            
    def toggle(self, toggle):
        """
        Changes the current toggle of the navbar.
        """
        self.navbar_current_toggle = toggle
        self.master.body.update_body(toggle)
    