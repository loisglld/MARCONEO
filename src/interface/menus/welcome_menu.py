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

        self.setup_headers()
        self.setup_buttons()

    def setup_headers(self) -> None:
        """
        Defines the labels used in the main menu.
        """
        self.title_lbl = Label(self, text="MARCONEO")
        self.config_frame = AppFrame(self)
        self.config_loaded_lbl = Label(self.config_frame, text="Config loaded: ")
        self.switch_config_btn = AppButton(self.config_frame, text="DEFAULT",
                                            command=self.switch_config)

        self.title_lbl.pack(side='top', pady=10, padx=10, fill="x")
        self.config_frame.pack(side='top', pady=10, padx=10, fill="x")
        self.config_loaded_lbl.pack(side='left', pady=10, padx=10, fill="x", expand=True)
        self.switch_config_btn.pack(side='right', pady=10, padx=10, fill="x", expand=True)

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the main menu.
        """
        self.custom_btn = AppButton(self, text="CUSTOM CONFIG",
                                      command=lambda: self.gui.change_menu(self.gui.settings_menu))
        self.credits_btn = AppButton(self, text="CREDITS",
                                     command=lambda: self.gui.change_menu(self.gui.credits_menu))

        self.load_btn = AppButton(self, text="LOAD",
                                   command=self.load_marco)
        self.power_btn = AppButton(self, text="POWER OFF",
                                   command=self.gui.app.close)

        self.custom_btn.pack(side="top", pady=10, padx=10, fill="x")
        self.credits_btn.pack(side="top", pady=10, padx=10, fill="x")

        self.power_btn.pack(side="bottom", pady=10, padx=10, fill="x")
        self.load_btn.pack(side="bottom", pady=10, padx=10, fill="x")
        return True

    def load_marco(self) -> None:
        """
        Changes the menu to the main menu.
        Config are already loaded, so it just
        changes the menu.
        """
        self.gui.app.config.load(self.gui.app.config.name)
        if self.gui.app.config.name == "custom":
            # if there is only the refill menu, it means that the user didn't change anything.
            if len(self.gui.app.config.get_loaded_categories()) <= 1:
                self.gui.loggers.log.warn("Config needs to be customed before loading it.")
                return
        self.gui.app.current_user.logout()
        self.gui.setup_menus()
        self.gui.change_menu(self.gui.main_menu)


    def switch_config(self) -> None:
        """
        Changes the menu to the main menu.
        """
        if self.gui.app.config.name == "custom":
            self.gui.app.config.name = self.gui.app.config.DEFAULT
            self.switch_config_btn.config(text="DEFAULT")
        elif self.gui.app.config.name == "default":
            self.gui.app.config.name = self.gui.app.config.CUSTOM
            self.switch_config_btn.config(text="CUSTOM")
        self.gui.loggers.log.info("Config switched to " + self.gui.app.config.name)
