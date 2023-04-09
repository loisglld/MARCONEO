"""
MemberCard.py

Member id card displayed on the window.
"""

#------------------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, Label

#------------------------------------------------------------------------------#

class MemberCard(Frame):
    def __init__(self, member, manager):
        super().__init__(manager)
        self.member = member
        self.manager =  manager
        self.loggers = self.manager.manager.manager.gui.loggers
        
        self.grid_propagate(False)
        self.configure(bg="#555555")
        
        self.setup_labels()
        
        self.create_card()
        
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
        
        self.first_name_label.grid(row=0, column=0, sticky='nsew')
        self.last_name_label.grid(row=0, column=1, sticky='nsew')
        self.balance_label.grid(row=0, column=2, sticky='nsew')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
    def setup_buttons(self):
        """
        Defines the buttons used in the menu.
        """
        return
        
    def create_card(self):
        pass
        
    def update_card(self):
        pass