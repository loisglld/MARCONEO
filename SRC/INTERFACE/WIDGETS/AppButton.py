"""
WButton.py

Configure MarcoNeo's app button.
"""

#-------------------------------------------------------------------#

from tkinter import Button

#-------------------------------------------------------------------#

class AppButton(Button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.configure(font=("System", 12), bg="#333333",
                       fg="#FFFFFF", activebackground="#555555",
                       activeforeground="#FFFFFF", bd=0, highlightthickness=0,
                       relief="flat", padx=10, pady=10)
