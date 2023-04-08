"""
Header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame
from SRC.INTERFACE.WIDGETS.MemberCard import MemberCard

#-------------------------------------------------------------------#


class Header(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.shopping_master = master.master
        self.loggers = self.shopping_master.gui.loggers
        self.member_card = MemberCard(self.shopping_master.gui.app.current_user, self)
        self.member_card.pack()
    
    def update_header(self):
        pass
