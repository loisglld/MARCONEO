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

        self.propagate(True)
        self.configure(bg="#555555")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.setup_labels()

    def setup_labels(self) -> bool:
        """
        Defines the labels used in the menu.
        """
        self.first_name_label = Label(self, text="-")
        self.last_name_label = Label(self, text="-")
        self.balance_label = Label(self, text="_")

        self.first_name_label.pack(side="top", fill="both", expand=True)
        self.last_name_label.pack(side="top", fill="both", expand=True)
        self.balance_label.pack(side="top", fill="both", expand=True)

        return True

    def update_card(self, member) -> None:
        """
        Updates the member card with
        the current member's informations.
        """
        if member.card_id is None:
            self.first_name_label.configure(text="-")
            self.last_name_label.configure(text="-")
            self.balance_label.configure(text="_")
            return
        self.first_name_label.configure(text=member.first_name)
        self.last_name_label.configure(text=member.last_name)
        self.balance_label.configure(text=member.balance)
