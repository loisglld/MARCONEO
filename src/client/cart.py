"""
cart.py

Describes the Cart class, which is used to
store the items caracteristics bought by a member.
"""

#-------------------------------------------------------------------#


class Cart:
    """
    Cart of the member logged on the current session.
    """
    def __init__(self, loggers, member=None):
        self.loggers = loggers
        self.member = member
        self.items = []
        self.total = 0

    def add_to_cart(self, item) -> None:
        """
        Adds an item to the cart.
        """
        self.items.append(item)

    def reset(self) -> None:
        """
        Resets the cart.
        """
        self.items = []
        self.total = 0

    def __str__(self) -> str:
        if self.member is None:
            return "No user is logged in."
        return f"Cart of {self.member.nickname}: {self.items.__str__()}"

    def __repr__(self) -> str:
        return self.__str__()
