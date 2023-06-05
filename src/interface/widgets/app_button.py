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
    DEFAULT_BG = "#A91B60"
    ACTIVE_TOGGLE = "#900C3F"
    def __init__(self, master=None, custom_theme:str="Red", **kwargs) -> None:
        Button.__init__(self, master, **kwargs)

        if custom_theme == "Red":
            self.configure(font=("System", 12), bg="#A91B60",
                            fg="#FFFFFF", activebackground="#DE026D",
                            activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                            relief="flat", padx=10, pady=10)
        elif custom_theme == "Green":
            self.configure(font=("System", 12), bg="#057A6D",
                            fg="#FFFFFF", activebackground="#019887",
                            activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                            relief="flat", padx=10, pady=10)
