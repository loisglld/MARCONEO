"""
MemberCard.py

Member id card displayed on the window.
"""

#------------------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label

#------------------------------------------------------------------------------#

class MemberCard(Frame):
    """
    Member card displayed on the window.
    """
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.manager =  manager
        self.loggers = self.manager.manager.manager.gui.loggers

        self.grid_propagate(False)
        self.configure(bg="#555555")

        self.setup_labels()

    def setup_labels(self) -> bool:
        """
        Defines the labels used in the menu.
        """
        self.first_name_label = Label(self, text="-")
        self.last_name_label = Label(self, text="-")
        self.balance_label = Label(self, text="_")

        self.first_name_label.pack()
        self.last_name_label.pack()
        self.balance_label.pack()

        return True

    def update_card(self, member):
        """
        Updates the member card with
        the current member's informations.
        """
        self.first_name_label.configure(text=member.first_name)
        self.last_name_label.configure(text=member.last_name)
        self.balance_label.configure(text=member.balance)
