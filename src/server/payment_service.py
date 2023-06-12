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


    def purchase(self):
        """
        Confirms the purchase.
        """
        if self.current_user.card_id is None:
            self.loggers.log.warning("No user is logged in. Can't purchase.")
            return

        for item in self.cart.items:
            print(item)
            id_member = self.current_user.id
            id_product = list(item.keys())[0]
            values = list(item.values())[0]
            price = values[1]
            quantity = values[0]
            self.current_user.balance -= price*quantity
            self.commit_purchase(id_product=id_product,
                                 id_member=id_member,
                                 price=price,
                                 quantity=quantity)

        self.app.cart.reset()
        self.loggers.log.debug("Cart has been reset.")
        self.app.update_user()

    def commit_purchase(self, id_product:int=None, id_member:int=None,
                        price:int=None, quantity:int=None) -> None:
        """
        Confirms the purchase.
        """
        self.app.db_cursor.update_balance(self.current_user)
        self.app.db_cursor.send_order(id_product=id_product,
                                        id_member=id_member,
                                        price=price,
                                        amount=quantity)

        self.loggers.log.info("Purchase confirmed. New balance of %s is %s€.",
                              self.current_user.first_name, self.current_user.balance)
        print(f"Purchase confirmed. Your new balance is {self.current_user.balance}€.")
