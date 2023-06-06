"""
price_modifier.py

This menu is made to allow Fouailles to change
the prices of products. Contains a digital keyboard
to enter the new prices.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, AppButton, LabelEntryPair

#-------------------------------------------------------------------#

class PriceModifier(Frame):
    """
    Price modifier menu.
    """
    def __init__(self, manager=None):
        super().__init__(manager)
        self.manager = manager
        self.shopping_manager = manager.manager
        self.loggers = self.shopping_manager.gui.app.loggers
        self.propagate(False)
        self.configure(bg="#555555")

        # Frames
        self.list_frame = Frame(self, bg="#ababab")
        self.control_frame = Frame(self, bg="#ababab")
        self.list_frame.pack(side='left', padx=10, pady=10, fill="both", expand=True)
        self.control_frame.pack(side='left', padx=10, pady=10, fill="both", expand=True)

        # Widgets
        self.setup_digital_keyboard(self.control_frame)
        self.back_btn = AppButton(self.control_frame, text="Back", command=self.back)
        self.back_btn.pack(padx=10, pady=10, fill="both", expand=True)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        current_toggle = self.shopping_manager.left_grid.navbar.current_toggle
        self.display_item_list(self.shopping_manager.retrieve_shopping_items(current_toggle))

    def show(self):
        """
        Shows the price modifier.
        """
        self.pack(side="top", fill="both", expand=True)
        self.manager.columnconfigure(0, weight=1)
        self.manager.rowconfigure(0, weight=1)

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
        if digit == 0:
            button.grid(row=3, column=1, padx=5, pady=5)
        elif digit in [7, 8, 9]:
            button.grid(row=0, column=digit-7, padx=5, pady=5)
        elif digit in [4, 5, 6]:
            button.grid(row=1, column=digit-4, padx=5, pady=5)
        elif digit in [1, 2, 3]:
            button.grid(row=2, column=digit-1, padx=5, pady=5)

    def setup_digital_keyboard(self, control_frame):
        """
        Sets up the digital keyboard.
        """
        keyboard_frame = Frame(control_frame, bg="#ababab")
        keyboard_frame.pack(padx=10, pady=10)

        for digit in range(1, 10):
            self.create_digit_button(keyboard_frame, digit)

        clear_button = AppButton(keyboard_frame, text="Suppr", width=5, height=2,
                                command=self.on_clear_click)
        clear_button.grid(row=3, column=0, padx=5, pady=5)

        zero_button = AppButton(keyboard_frame, text="0", width=5, height=2,
                                command=lambda: self.on_digit_click(0))
        zero_button.grid(row=3, column=1, padx=5, pady=5)

        enter_button = AppButton(keyboard_frame, text="Entrer", width=5, height=2,
                                command=self.on_enter_click)
        enter_button.grid(row=3, column=2, padx=5, pady=5)

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

    def display_item_list(self, items):
        """
        Displays the items in the list.
        """
        for item in items:
            LabelEntryPair(self.list_frame,
                           text=item["name"],
                           entry_text=str(item["price"])).pack(fill="x", padx=10, pady=10)
