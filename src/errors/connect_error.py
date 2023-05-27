"""
connect_error.py

Defines the ConnectError class.
"""

class ConnectError(Exception):
    """
    ConnectError class.
    """

    def __init__(self, message):
        """
        ConnectError class's constructor.
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        """
        ConnectError class's string representation.
        """
        return repr(self.message)