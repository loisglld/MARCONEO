"""
right_sett.py

Right side of the setting page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame
from src.interface.menus.settings.right.sett_header import SettHeader
from src.interface.menus.settings.right.sett_body import SettBody
from src.interface.menus.settings.right.sett_footer import SettFooter

#-------------------------------------------------------------------#

class RightSett(Frame):
    """
    Container of the header, body and footer of the shopping page.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager
        self.propagate(False)

        self.header = SettHeader(self)
        self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.body = SettBody(self)
        self.body.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.footer = SettFooter(self)
        self.footer.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)
