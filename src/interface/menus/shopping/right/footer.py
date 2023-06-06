"""
footer.py

Describes the footer of the shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton, Label

#-------------------------------------------------------------------#

class Footer(Frame):
    """
    Footer of the shopping menu.
    Contains the confirm button and the reset button
    and the total of the cart.
    """
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
        self.price_modifier_btn = AppButton(self, text="Price modifier", command=self.modify_prices)

        self.reset_btn.pack(side="left", padx=10)
        self.total_label.pack(side="left", padx=10)
        self.confirm_btn.pack(side="right", padx=10)
        self.price_modifier_btn.pack(side="right", padx=10)

    def reset(self):
        """
        Reset the page.
        """
        if not self.cart.total:
            return
        self.cart.reset()
        self.update_footer()
        self.shopping_manager.right_grid.body.update_body(
            self.shopping_manager.left_grid.navbar.current_toggle)
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
        if not self.cart.total:
            return

        if self.shopping_manager.gui.app.current_user.balance < self.cart.total:
            self.loggers.log.warning("Not enough money to purchase.")
            return

        self.confirm_btn.configure(text="Sure?", command=self.do_purchase)

    def do_purchase(self):
        """
        Does the purchase.
        """
        self.shopping_manager.gui.app.payment_service.commit_purchase()
        self.shopping_manager.right_grid.body.update_body(
            self.shopping_manager.left_grid.navbar.current_toggle)
        self.reset()
        self.confirm_btn.configure(text="Confirm", command=self.confirm_purchase)

    def modify_prices(self):
        """
        Opens the price modifier menu.
        """
        self.shopping_manager.right_grid.price_modifier.show()
