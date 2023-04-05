"""
Header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame
from SRC.INTERFACE.WIDGETS.MemberCard import MemberCard

#-------------------------------------------------------------------#


class Header(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.loggers = self.master.gui.loggers
        self.member_card = MemberCard(self.master.gui.app.current_user, self.master)
    
    def update_header(self):
        pass
