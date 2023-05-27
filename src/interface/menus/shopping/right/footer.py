"""
footer.py

Describes the footer of the shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton, Label

#-------------------------------------------------------------------#

class Footer(Frame):
    def __init__(self, manager=None):
        super().__init__(manager)
        self.shopping_manager = manager.manager
        self.loggers = self.shopping_manager.gui.app.loggers
        self.grid_propagate(False)
        self.configure(bg="#555555")

        self.cart = self.shopping_manager.gui.app.cart

        self.setup_container()

    def setup_container(self):
        """
        Sets up the container of the footer.
        """
        self.confirm_btn = AppButton(self, text="Confirm", command=self.confirm_purchase)
        self.reset_btn = AppButton(self, text="Reset cart", command=self.reset)
        self.total_label = Label(self, text=f"Cart: {self.cart.total}")

        self.total_label.grid(row=0, column=0, sticky='nsew')
        self.reset_btn.grid(row=0, column=1, sticky='nsew')
        self.confirm_btn.grid(row=0, column=2, sticky='nsew')

    def reset(self):
        """
        Reset the page.
        """
        if not self.cart.total:
            return
        self.cart.reset()
        self.shopping_manager.right_grid.body.update_body(self.shopping_manager.current_toggle)
        self.update_footer()
        self.loggers.log.debug("Cart has been reset.")

    def update_footer(self):
        """
        Updates the total label.
        """
        self.total_label.configure(text=f"Cart: {self.cart.total}")

    def confirm_purchase(self):
        """
        Confirms the purchase.
        """
        self.shopping_manager.gui.app.payment_service.confirm_purchase()
        self.reset()
