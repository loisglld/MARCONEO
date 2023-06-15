"""
footer.py

Describes the footer of the shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label, ImageButton

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
        self.propagate(False)
        self.configure(bg="#000000", borderwidth=5, border=5,
                    highlightbackground="#4d88ff", highlightthickness=5)
        self.cart = self.shopping_manager.gui.app.cart

        self.setup_container()

    def setup_container(self):
        """
        Sets up the container of the footer.
        """
        self.confirm_btn = ImageButton(self, image=self.shopping_manager.gui.confirm, command=self.confirm_purchase)
        self.reset_btn = ImageButton(self, image=self.shopping_manager.gui.discard, command=self.reset)


        cart_frame = Frame(self, bg="black")
        self.cart_img = Label(cart_frame, image=self.shopping_manager.gui.cart,
                              bg="black", border=0,
                              borderwidth= 0, highlightthickness=0)
        self.total_label = Label(cart_frame, text=f"{self.cart.total} €",
                                 font=("System", 20, "bold"), bg="black", fg="white")
        self.cart_img.pack(side="left", padx=10)
        self.total_label.pack(side="left", padx=10)

        cart_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.reset_btn.place(relx=0.02, rely=0.5, anchor="w")
        self.confirm_btn.place(relx=0.98, rely=0.5, anchor="e")

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

    def update_footer(self):
        """
        Updates the total label.
        """
        self.total_label.configure(text=f"{self.cart.total} €")
        if self.cart.total>self.shopping_manager.gui.app.current_user.balance:
            self.total_label.configure(fg="red")
        else:
            self.total_label.configure(fg="white")

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
        self.shopping_manager.gui.app.payment_service.purchase()
        self.shopping_manager.gui.app.cart.reset()
        self.loggers.log.debug("Cart has been reset.")
        self.shopping_manager.gui.app.update_user()
        self.shopping_manager.right_grid.body.update_body(
            self.shopping_manager.left_grid.navbar.current_toggle)
        self.reset()
        self.confirm_btn.configure(command=self.confirm_purchase)
