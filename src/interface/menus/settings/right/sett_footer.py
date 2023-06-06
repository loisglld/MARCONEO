"""
sett_footer.py

Footer of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#

class SettFooter(Frame):
    """
    Footer of the settings page of the app.
    """
    def __init__(self, manager=None) -> None:
        super().__init__(manager)
        self.manager = manager
        self.propagate(False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
