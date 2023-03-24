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
        self.total = 0
        
    def add_to_cart(self, item):
        self.items.append(item)
        
    def reset(self):
        self.items = []
        self.total = 0
        
    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price    
        
    def get_total(self):
        total = 0
        print("--------------------")
        for item in self.items:
            print(item.__str__())
            total += item.amount
        self.total = total
        return total
    