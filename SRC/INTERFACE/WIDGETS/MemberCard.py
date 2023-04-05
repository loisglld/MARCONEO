"""
MemberCard.py

Member id card displayed on the window.
"""

#------------------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label

#------------------------------------------------------------------------------#

class MemberCard(Frame):
    def __init__(self, member, master):
        super().__init__(master)
        self.member = member
        self.master =  master
        self.loggers = self.master.gui.loggers
        self.grid_propagate(False)
        self.configure(bg="#555555")
        
        self.setup_labels()
        
        self.card = self.create_card()
        
    def setup_images(self):
        """
        Defines the images used in the menu.
        """
        return
    
    def setup_labels(self):
        """
        Defines the labels used in the menu.
        """        
        
        
        self.first_name_label = Label(self, text="-")
        self.last_name_label = Label(self, text="-")
        self.balance_label = Label(self, text="_")
        
        self.first_name_label.pack()
        self.last_name_label.pack()
        self.balance_label.pack()
        
        
        
    def setup_buttons(self):
        """
        Defines the buttons used in the menu.
        """
        return
        
    def create_card(self):
        pass
        
    def update_card(self):
        pass