"""
Header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.utils.gui_utils import Frame
from SRC.INTERFACE.WIDGETS.MemberCard import MemberCard

#-------------------------------------------------------------------#


class Header(Frame):
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager
        self.shopping_manager = manager.manager
        
        self.grid_propagate(False)
        self.configure(bg="#555555")
        
        self.loggers = self.shopping_manager.gui.loggers
        self.member_card = MemberCard(self.shopping_manager.gui.app.current_user, self)
        self.member_card.grid(row=0, column=0, sticky='nsew')
    
    def update_header(self):
        pass
