"""
button_app.py

Configure MarcoNeo's app button.
"""

#-------------------------------------------------------------------#

from tkinter import Button

#-------------------------------------------------------------------#

class AppButton(Button):
    """
    Custom button for MarcoNeo's app.
    """
    DEFAULT_BG = "#555555"
    ACTIVE_TOGGLE = "#999999"
    def __init__(self, master=None, **kwargs) -> None:
        Button.__init__(self, master, **kwargs)
        self.configure(font=("System", 12), bg=self.DEFAULT_BG,
                            fg="#FFFFFF", activebackground="#777777",
                            activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                            relief="flat", padx=10, pady=10)

class ImageButton(Button):
    """
    Custom button for MarcoNeo's app.
    """
    def __init__(self, master=None, **kwargs) -> None:
        Button.__init__(self, master, **kwargs)
        self.configure( bg="#000000", activebackground="#000000",
                        activeforeground="#000000", bd=0,
                        highlightthickness=0)
