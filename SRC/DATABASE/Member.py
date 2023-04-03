"""
Member.py

Defines the Member class 
and everything related to the member
of the BDE of Télécom Physique Strasbourg.
"""

#-------------------------------------------------------------------#

#-------------------------------------------------------------------#

class Member:
    def __init__(self, loggers, member_data: dict):
        self.loggers = loggers
        self.member_data = member_data
        
        self.first_name = member_data['first_name']
        self.last_name = member_data['last_name']
        self.nickname = member_data['nickname']
        self.card_id = member_data['card_id']
        self.balance = member_data['balance']
        self.is_admin = member_data['is_admin']
        self.is_contributor = member_data['is_contributor']
        
        print(f"Current user: {self.first_name} {self.last_name}")  
        self.loggers.log.info(f"Current user: {self.first_name} {self.last_name}")
        
    def __str__(self):
        print(self.member_data)
        if self.member_data is None:
            return "No user is logged in."
        return f"{self.first_name} {self.last_name} ({self.nickname})"
    
    def __repr__(self):
        return self.__str__()
