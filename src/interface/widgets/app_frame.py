"""
app_frame.py


Contains the custom frame class used
in the application's GUI.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#

class AppFrame(Frame):
    """
    Custom frame class used in the application's GUI.
    """
    DARK = "#111111"
    DARKGRAY = "#333333"
    GRAY = "#555555"
    LIGHTGRAY = "#777777"
    LIGHT = "#999999"
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.config(bg=self.DARK)
