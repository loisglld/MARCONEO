"""
Footer.py

Describes the footer of the shopping menu.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.gui_utils import Frame, AppButton, Label

#-------------------------------------------------------------------#

class Footer(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.shopping_master = master
        self.grid_propagate(False)
        self.configure(bg="#555555")
        
        self.cart = self.shopping_master.gui.app.current_user.cart
        self.total = str(self.cart.total)
        
        self.setup_container()
        
    def setup_container(self):
        """
        Sets up the container of the footer.
        """
        self.confirm_btn = AppButton(self, text="Confirm", command=self.confirm_purchase)
        self.reset_btn = AppButton(self, text="Reset cart", command=self.reset_cart)
        self.total_label = Label(self, text=f"Cart: {self.total}")
        
        self.total_label.pack()
        self.reset_btn.pack()
        self.confirm_btn.pack()
        
    def reset_cart(self):
        """
        Reset the cart.
        """
        self.cart.reset()
        self.shopping_master.body.update_body(self.shopping_master.current_toggle)
        self.update_total_label(self.cart.total)
        
    def update_total_label(self, total=None):
        """
        Updates the total label.
        """
        self.total_label.configure(text=f"Cart: {total}")
    
    def confirm_purchase(self):
        """
        Confirms the purchase.
        """
        self.shopping_master.gui.app.current_user.confirm_purchase()
        self.reset_cart()
    