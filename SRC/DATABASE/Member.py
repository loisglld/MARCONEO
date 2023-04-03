"""
Member.py

Defines the Member class 
and everything related to the member
of the BDE of Télécom Physique Strasbourg.
"""

#-------------------------------------------------------------------#

from SRC.DATABASE.Cart import Cart

#-------------------------------------------------------------------#

class Member:
    def __init__(self, loggers, member_data: dict):
        self.loggers = loggers
        self.member_data = member_data
        
        if self.member_data is None:
            self.cart = Cart(self)
            
            print("No user is logged in.")
            self.loggers.log.info("No user is logged in.")
            return
        
        self.first_name = member_data['first_name']
        self.last_name = member_data['last_name']
        self.nickname = member_data['nickname']
        self.card_id = member_data['card_id']
        self.balance = member_data['balance']
        self.is_admin = member_data['is_admin']
        self.is_contributor = member_data['is_contributor']
        self.cart = Cart(self)
        
        print(f"Current user: {self.first_name} {self.last_name}")  
        self.loggers.log.info(f"Current user: {self.first_name} {self.last_name}")
        
    def confirm_purchase(self):
        """
        Confirms the purchase.
        """
        print(self.cart.total)
        if self.member_data is None:
            self.loggers.log.warning("No user is logged in. Can't purchase the cart.")
            return
        self.balance -= self.cart.total
        print(f"Purchase confirmed. Your new balance is {self.balance}€.")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nickname})"
    
    def __repr__(self):
        return self.__str__()
