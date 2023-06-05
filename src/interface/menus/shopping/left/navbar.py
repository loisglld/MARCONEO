"""
Nabar.py

Configure MarcoNeo's navbar on its shopping menu.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton

#-------------------------------------------------------------------#

class Navbar(Frame):
    """
    Contains the different toggles of the shopping menu.
    Is used to navigate between the different toggles.
    """
    def __init__(self, left_grid=None):
        super().__init__(left_grid)
        self.manager = left_grid
        self.current_toggle = "Party"
        self.party_btn = None
        self.shopping_menus = list(self.manager.manager.gui.app.config['Shopping'].keys())

        self.grid_propagate(False)
        self.configure(bg="black")
        self.setup_buttons()

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the menu.
        """
        for menu in self.shopping_menus:
            button = AppButton(self, text=menu, command=lambda menu=menu: self.toggle(menu))
            setattr(self, f"{menu.lower()}_btn", button)
            button.pack(fill="both", expand=True, side="top", padx=10, pady=10)

        self.party_btn.configure(bg=AppButton.ACTIVE_TOGGLE)  # set active toggle color
        self.back_btn = AppButton(self, text="Back",
                                  command=lambda: self.manager.manager.gui.change_menu(
                                      self.manager.manager.gui.main_menu))
        self.back_btn.pack(fill="both", expand=True, side="bottom", padx=10, pady=10)
        return True

    def toggle(self, toggle: str) -> None:
        """
        Changes the current toggle of the navbar.
        """
        self.current_toggle = toggle

        # Update button's colors
        for menu in self.shopping_menus:
            button = getattr(self, f"{menu.lower()}_btn")
            if menu == self.current_toggle:
                button.configure(bg=AppButton.ACTIVE_TOGGLE)  # set active toggle color
            else:
                button.configure(bg=AppButton.DEFAULT_BG)  # set default color


        self.manager.manager.right_grid.body.update_body(toggle)
        self.manager.manager.right_grid.footer.reset()
