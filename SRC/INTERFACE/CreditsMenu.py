"""
CreditsMenu.py.py

Configure MarcoNeo's credits page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class CreditsMenu(tk.Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        self.gui.loggers.log.debug("(Credits menu)")
        
        self.credits = """Contributors:\nMarc Mounissens\nClément Rossetti
Hugo Chambon, Nathan Favriou, Jade Touresse\nYannick Hénin\nGatien Chenu, Mathieu Martin\nLoïs Gallaud"""
        
        self.credits_label = tk.Label(self, text=self.credits)
        self.credits_label.pack()
        