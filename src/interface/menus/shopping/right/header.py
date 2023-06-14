"""
header.py

Top section of the shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton
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
        self.logout_btn = AppButton(self, text="Déconnexion", command=self.logout)
        self.logout_btn.pack(side="bottom", fill="both", expand=True)

    def logout(self) -> None:
        """
        Log out the current user and update the page.
        """
        self.shopping_manager.gui.app.cart.reset()
        self.shopping_manager.gui.app.update_user()
        footer =  self.shopping_manager.right_grid.footer
        self.manager.manager.gui.app.current_user.logout()
        self.shopping_manager.right_grid.body.update_body(
            self.shopping_manager.left_grid.navbar.current_toggle)
        footer.reset()
        footer.confirm_btn.configure(text="Confirm", command=footer.confirm_purchase)

        self.loggers.log.info("User logged out.")
