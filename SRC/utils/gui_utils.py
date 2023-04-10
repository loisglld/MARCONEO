"""
gui_utils.py

Defines the tkinter classes that are used in the application.
Helps to reduce the number of imports in the other files.
"""

#-------------------------------------------------------------------#

from tkinter import Tk, Frame, Label, Entry, BOTH
from SRC.INTERFACE.WIDGETS.AppButton import AppButton

#-------------------------------------------------------------------#

__all__ = ['Tk', 'Frame', 'Label', 'AppButton', 'Entry', 'BOTH']
