"""
main_menu.py

Configure MarcoNeo's welcome page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import AppButton, AppFrame, AppLabel, ImageButton
from src.interface.menus.shopping.shopping_menu import ShoppingMenu

#-------------------------------------------------------------------#

class MainMenu(AppFrame):
    """
    MarcoNeo's main page.

    It is the first page to appear
    when the application is launched.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui

        self.title = AppLabel(self, image=self.gui.logo)
        self.config_frame = AppFrame(self)
        self.config_loaded_lbl = AppLabel(self.config_frame, text="Config loaded: ")
        self.switch_config_btn = AppButton(self.config_frame, text="DEFAULT",
                                            command=self.switch_config)
        self.config_loaded_lbl.propagate(False)
        self.switch_config_btn.propagate(False)

        self.custom_btn = ImageButton(self, image=self.gui.configuration,
                                command=lambda: self.gui.change_menu(self.gui.settings_menu))
        self.credits_btn = ImageButton(self, image=self.gui.credits,
                                    command=lambda: self.gui.change_menu(self.gui.credits_menu))
        self.history_btn = ImageButton(self, image=self.gui.history,
                                    command=self.history)
        self.load_btn = ImageButton(self, image=self.gui.load,
                                command=self.load_marco)
        self.power_btn = ImageButton(self, image=self.gui.poweroff,
                                command=self.gui.app.close)


        self.title.place(relx=0.5, rely=0.3, anchor="center")

        self.load_btn.place(relx=0.5, rely=0.65, anchor="center")
        self.config_frame.place(relx=0.5, rely=0.9, anchor="center")
        self.config_loaded_lbl.pack(side='left', pady=10, padx=10, fill="x")
        self.switch_config_btn.pack(side='right', pady=10, padx=10, fill="x")

        self.power_btn.place(relx=0.03, rely=0.97, anchor="sw")
        self.credits_btn.place(relx=0.15, rely=0.97, anchor="sw")

        self.history_btn.place(relx=0.97, rely=0.97, anchor="se")
        self.custom_btn.place(relx=0.85, rely=0.97, anchor="se")

    def load_marco(self) -> None:
        """
        Changes the menu to the main menu.
        Config are already loaded, so it just
        changes the menu.
        """
        # Security check
        if self.gui.app.config is None:
            self.gui.app.loggers.log.warn("There is no config file loaded.")
            return

        self.gui.app.config.update_loaded_config()
        # Security check for custom config
        if self.gui.app.config.name == self.gui.app.config.CUSTOM:
            # if there is only the refill menu, it means that the user didn't change anything.
            if len(self.gui.app.config.get_custom_categories()) <= 1:
                self.gui.loggers.log.warn("Config needs to be customed before loading it.")
                return

        # Fresh new start
        self.gui.app.current_user.logout()
        self.gui.shopping_menu = ShoppingMenu(self.gui)
        self.gui.change_menu(self.gui.shopping_menu)

    def switch_config(self) -> None:
        """
        Changes the menu to the main menu.
        """
        custom = self.gui.app.config.CUSTOM
        default = self.gui.app.config.DEFAULT
        if self.gui.app.config.name == custom:
            self.gui.app.config.name = default
            self.switch_config_btn.config(text="DEFAULT")
        elif self.gui.app.config.name == default:
            self.gui.app.config.name = custom
            self.switch_config_btn.config(text="CUSTOM")
        self.gui.loggers.log.info("Config switched to " + self.gui.app.config.name)

    def history(self) -> True:
        """
        Change menu to history menu.
        """
        self.gui.history_menu.refresh_history()
        self.gui.change_menu(self.gui.history_menu)
        return True
