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
    def __init__(self, member_data: dict):
        if member_data is None:
            self.last_name = None
            self.first_name = None
            self.nickname = None
            self.card_id = None
            self.balance = None
            self.is_admin = None
            self.is_contributor = None
            self.cart = Cart(self)
            return
        
        self.last_name = member_data['last_name']
        self.first_name = member_data['first_name']
        self.nickname = member_data['nickname']
        self.card_id = member_data['card_id']
        self.balance = member_data['balance']
        self.is_admin = member_data['is_admin']
        self.is_contributor = member_data['is_contributor']
        self.cart = Cart(self)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nickname})"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.nickname})"
