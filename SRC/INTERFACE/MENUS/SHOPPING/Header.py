"""
Header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame
from SRC.INTERFACE.WIDGETS.MemberCard import MemberCard

#-------------------------------------------------------------------#


class Header(Frame):
    def __init__(self, rigth_grid):
        super().__init__(rigth_grid)
        self.master = rigth_grid.master
        self.loggers = self.master.gui.loggers
        self.member_card = MemberCard(self.master.gui.app.current_user, self)
        self.member_card.pack()
    
    def update_header(self):
        pass
