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
    
    def __str__(self):
        return f"Cart of {self.member.nickname}: {self.items.__str__()}"
    
    def __repr__(self):
        return self.__str__()
    