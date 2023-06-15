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
        self.gui_manager = manager.manager.manager.gui
        self.loggers = self.gui_manager.loggers

        self.configure(bg="#000000")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.setup_labels()

    def setup_labels(self) -> bool:
        """
        Defines the labels used in the menu.
        """
        self.name_label = Label(self, text="-",
                                      font=("system", 12), fg="#ffffff", bg="#000000")
        self.balance_label = Label(self, text="_", fg="gold",
                                   font=("system", 12, "bold"), bg="#000000")

        self.name_label.pack(padx=5, pady=10)
        self.balance_label.pack(padx=5, pady=(0, 5))

        return True

    def update_card(self, member) -> None:
        """
        Updates the member card with
        the current member's informations.
        """
        if member.admin:
            self.loggers.log.warning("Member %s is an admin.", member.first_name)
            self.manager.id_card.configure(image=self.gui_manager.crown)
        elif not member.contributor:
            self.loggers.log.warning("Member %s is not a contributor.", member.first_name)
            self.manager.id_card.configure(image=self.gui_manager.warning)
        else:
            self.manager.id_card.configure(image=self.gui_manager.id)
        if member.card_id is None:
            self.name_label.configure(text="-")
            self.balance_label.configure(text="_")
            return
        self.name_label.configure(text=member.first_name + " " + member.last_name)
        self.balance_label.configure(text=f"{member.balance}€")
