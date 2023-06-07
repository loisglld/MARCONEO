"""
welcome_menu.py

Configure MarcoNeo's welcome page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Label, AppButton, AppFrame

#-------------------------------------------------------------------#

class WelcomeMenu(AppFrame):
    """
    MarcoNeo's welcome page.

    It is the first page to appear
    when the application is launched.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

        self.setup_label()
        self.setup_buttons()

    def setup_label(self) -> None:
        """
        Defines the labels used in the main menu.
        """
        Label(self, text="Welcome to MarcoNeo").pack()
        self.config_loaded_lbl = Label(self, text=f"Config loaded: {self.gui.app.config.name}")
        self.config_loaded_lbl.pack()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the main menu.
        """
        self.settings_btn = AppButton(self, text="CONFIGURATION",
                                      command=lambda: self.gui.change_menu(self.gui.settings_menu))
        self.credits_btn = AppButton(self, text="CREDITS",
                                     command=lambda: self.gui.change_menu(self.gui.credits_menu))

        self.load_btn = AppButton(self, text="LOAD",
                                   command=self.enter_marco)
        self.power_btn = AppButton(self, text="POWER OFF",
                                   command=self.gui.app.close)

        self.settings_btn.pack(side="top", pady=10, padx=10, fill="x")
        self.credits_btn.pack(side="top", pady=10, padx=10, fill="x")

        self.power_btn.pack(side="bottom", pady=10, padx=10, fill="x")
        self.load_btn.pack(side="bottom", pady=10, padx=10, fill="x")
        return True

    def enter_marco(self) -> None:
        """
        Changes the menu to the main menu.
        """
        self.gui.app.config.load(self.gui.app.config.name)
        if self.gui.app.config == {}:
            self.gui.loggers.log.fatal("No config file found.")
            return
        self.gui.setup_menus()
        self.gui.change_menu(self.gui.main_menu)
