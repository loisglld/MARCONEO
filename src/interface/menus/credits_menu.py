"""
credits_menu.py

Configure MarcoNeo's credits page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppFrame, Label, AppButton

#-------------------------------------------------------------------#

class CreditsMenu(AppFrame):
    """
    MarcoNeo's credits page.

    It contains every contributor to the project.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui
        #self.gui.loggers.log.debug("(Credits menu)")

        self.credits = """Contributors:\nMarc Mounissens\nClément Rossetti
Hugo Chambon, Nathan Favriou, Jade Touresse\nYannick Hénin\nGatien Chenu, Mathieu Martin\nLoïs Gallaud"""

        self.credits_label = Label(self, text=self.credits)
        self.back_btn = AppButton(self, text="Back",
                                  command=lambda: self.gui.change_menu(self.gui.welcome_menu))

        self.credits_label.pack()
        self.back_btn.pack()
