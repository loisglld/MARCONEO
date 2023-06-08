"""
header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame
from src.interface.widgets.member_card import MemberCard

#-------------------------------------------------------------------#


class Header(Frame):
    """
    Top section of the shopping menu.
    """
    def __init__(self, manager=None) -> None:
        super().__init__(manager)
        self.manager = manager
        self.shopping_manager = manager.manager
        self.loggers = self.shopping_manager.gui.loggers
        self.propagate(True)
        self.configure(bg="#555555")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.member_card = MemberCard(self)
        self.member_card.pack(side="top", fill="both", expand=True)
