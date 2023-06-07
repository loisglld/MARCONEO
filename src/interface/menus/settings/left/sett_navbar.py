"""
sett_navbar.py

Navbar of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton

#-------------------------------------------------------------------#

class SettNavbar(Frame):
    """
    Navbar of the settings page of the app.
    """
    def __init__(self, left_grid=None):
        super().__init__(left_grid)
        self.manager = left_grid
        self.config(bg="#000000")
        self.back_btn = None
        self.current_toggle = "Lunch"
        self.categories = list(self.manager.manager.gui.app.config.api_config.keys())
        self.setup_buttons()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the navbar.
        """
        for menu in self.categories:
            button = AppButton(self, text=menu, command=lambda menu=menu: self.toggle(menu))
            setattr(self, f"{menu.lower()}_btn", button)
            button.pack(fill="both", expand=True, side="top", padx=10, pady=10)
        self.back_btn = AppButton(self, text="Back",
                                    command=lambda:
                                        self.manager.manager.gui.change_menu(
                                            self.manager.manager.gui.welcome_menu))

        self.back_btn.pack(side="bottom", pady=10, padx=10, fill="x")

    def toggle(self, toggle: str) -> None:
        """
        Changes the current toggle of the navbar.
        """
        self.current_toggle = toggle

        # Update button's colors
        for menu in self.categories:
            button = getattr(self, f"{menu.lower()}_btn")
            if menu == self.current_toggle:
                button.configure(bg=AppButton.ACTIVE_TOGGLE)  # set active toggle color
            else:
                button.configure(bg=AppButton.DEFAULT_BG)  # set default color

        self.manager.manager.right_grid.body.update_body(toggle)
