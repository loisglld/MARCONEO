"""
gui_utils.py

Defines the tkinter classes that are used in the application.
Helps to reduce the number of imports in the other files.
"""

#-------------------------------------------------------------------#

from tkinter import Frame, Label, Entry, BOTH
from SRC.INTERFACE.WIDGETS.AppButton import AppButton

#-------------------------------------------------------------------#

__all__ = ['Frame', 'Label', 'WButton', 'Entry', 'BOTH']
