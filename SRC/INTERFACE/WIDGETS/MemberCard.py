"""
MemberCard.py

Member id card displayed on the window.
"""

#------------------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame

#------------------------------------------------------------------------------#

class MemberCard(Frame):
    def __init__(self, member, master):
        self.member = member
        self.loggers = self.master.loggers
        self.first_name = self.member.first_name
        self.last_name = self.member.last_name
        
        self.card = self.create_card()
        
    def create_card(self):
        pass
        
    def update_card(self):
        pass