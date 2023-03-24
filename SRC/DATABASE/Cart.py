"""
Cart.py

Describes the Cart class, which is used to
store the items caracteristics bought by a member.
"""

#-------------------------------------------------------------------#
#-------------------------------------------------------------------#

class Cart:
    def __init__(self, member):
        self.member = member
        self.items = []
        self.total_price = 0
        
    def add_to_cart(self, item):
        self.items.append(item)
        
    def reset(self):
        self.items = []
        self.total = 0   
        
    def get_total_price(self):
        total = 0
        print("--------------------")
        for item in self.items:
            print(item.__str__())
            total += item.amount * item.price
        self.total_price = total
        return total
    
    def __str__(self):
        return f"Cart of {self.member.nickname}: {self.items.__str__()}"
    