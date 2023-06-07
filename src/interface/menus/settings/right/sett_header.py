"""
sett_header.py

Header of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class SettHeader(Frame):
    """
    Header of the settings page of the app.
    """
    def __init__(self, manager=None) -> None:
        super().__init__(manager)
        self.manager = manager
        self.propagate(False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        Label(self,
                text="CUSTOM YOUR MARCO").pack(side="left",
                                        expand=True)
        Label(self,
              text="Select item by clicking on them. \n(Green: item selected)").pack(side="left",
                                                                                    expand=True)
