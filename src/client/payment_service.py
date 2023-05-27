"""
payment_service.py

Defines the PaymentService class.
Let the user pay for his purchases.
"""

#-------------------------------------------------------------------#


#-------------------------------------------------------------------#

class PaymentService:
    """
    Defines the PaymentService class.
    """
    def __init__(self, app) -> None:
        self.app = app
        self.current_user = app.current_user
        self.cart = self.app.cart
        self.loggers = app.loggers

    def confirm_purchase(self):
        """
        Confirms the purchase.
        """
        if self.current_user is None:
            self.loggers.log.warning("No user is logged in. Can't purchase.")
            return
        self.current_user.balance -= self.cart.total
        self.app.db_cursor.update_balance(self.current_user)

        self.app.update_user()

        self.loggers.log.info("Purchase confirmed. New balance of %s is %s€.",
                              self.current_user.first_name, self.current_user.balance)
        print(f"Purchase confirmed. Your new balance is {self.current_user.balance}€.")