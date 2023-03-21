"""
CreditsMenu.py.py

Configure MarcoNeo's credits page.
"""

#-------------------------------------------------------------------#

from SRC.INTERFACE.tkinter_utils import Frame, Label

#-------------------------------------------------------------------#

class CreditsMenu(Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        #self.gui.loggers.log.debug("(Credits menu)")
        
        self.credits = """Contributors:\nMarc Mounissens\nClément Rossetti
Hugo Chambon, Nathan Favriou, Jade Touresse\nYannick Hénin\nGatien Chenu, Mathieu Martin\nLoïs Gallaud"""
        
        self.credits_label = Label(self, text=self.credits)
        self.credits_label.pack()
        