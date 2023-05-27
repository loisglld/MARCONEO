"""
gui_utils.py

Defines the tkinter classes that are used in the application.
Helps to reduce the number of imports in the other files.
"""

#-------------------------------------------------------------------#

from tkinter import Tk, Frame, Label, Entry, BOTH
from src.interface.widgets.app_button import AppButton
from src.interface.widgets.app_frame import AppFrame

#-------------------------------------------------------------------#

__all__ = ['Tk', 'Frame', 'Label', 'AppButton',
           'Entry', 'BOTH', 'AppFrame', 'AppButton']
