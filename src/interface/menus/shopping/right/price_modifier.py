"""
price_modifier.py

This menu is made to allow Fouailles to change
the prices of products. Contains a digital keyboard
to enter the new prices.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton

#-------------------------------------------------------------------#

class PriceModifier(Frame):
    """
    Price modifier menu.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.shopping_manager = manager.manager
        self.loggers = self.shopping_manager.gui.app.loggers
        self.grid_propagate(False)
        self.configure(bg="#555555")

        self.back_btn = AppButton(self, text="Back", command=self.back)
        self.back_btn.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        self.setup_digital_keyboard()

    def on_digit_click(self, digit):
        """
        Prints the digit clicked.
        """
        print(f"Digit clicked: {digit}")

    def on_clear_click(self):
        """
        Clears the digital keyboard.
        """
        print("Clear clicked")

    def on_enter_click(self):
        """
        Confirms the new price.
        """
        print("Enter clicked")

    def create_digit_button(self, frame, digit):
        """
        Creates a digit button.
        """
        button = AppButton(frame, text=str(digit), width=5, height=2,
                        command=lambda: self.on_digit_click(digit))
        button.grid(row=digit//3, column=digit%3, padx=5, pady=5)

    def setup_digital_keyboard(self):
        """
        Sets up the digital keyboard.
        """
        keyboard_frame = Frame(self, bg="#ababab")
        keyboard_frame.pack(padx=10, pady=10)

        for digit in range(10):
            self.create_digit_button(keyboard_frame, digit)

        clear_button = AppButton(keyboard_frame, text="Suppr", width=5, height=2,
                                command=self.on_clear_click)
        clear_button.grid(row=3, column=0, padx=5, pady=5)

        enter_button = AppButton(keyboard_frame, text="Entrer", width=5, height=2,
                                command=self.on_enter_click)
        enter_button.grid(row=3, column=1, padx=5, pady=5)


    def back(self):
        """
        Goes back to the shopping menu.
        """
        self.pack_forget()
        self.shopping_manager.right_grid.header.grid(row=0, column=0, sticky='nsew')
        self.shopping_manager.right_grid.body.grid(row=1, column=0, sticky='nsew')
        self.shopping_manager.right_grid.footer.grid(row=2, column=0, sticky='nsew')
        self.shopping_manager.right_grid.body.update_body(
            self.shopping_manager.left_grid.navbar.current_toggle)
        self.loggers.log.debug("Price modifier has been closed.")
