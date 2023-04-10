"""
closing_error.py

Defines the ClosingError class.
"""

class ClosingError(Exception):
    """
    ClosingError class.
    """

    def __init__(self, message):
        """
        ClosingError class's constructor.
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        """
        ClosingError class's string representation.
        """
        return repr(self.message)