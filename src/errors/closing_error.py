"""
closing_error.py

Defines the ClosingError class.
"""

class ClosingError(Exception):
    """
    ClosingError class.
    """

    def __init__(self, message, error_code=None) -> None:
        """
        ClosingError class's constructor.
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self) -> str:
        if self.error_code:
            return f"ClosingError (Error Code: {self.error_code}): {super().__str__()}"
        else:
            return f"ClosingError: {super().__str__()}"
