"""
sett_item.py

Item of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class SettItem(Frame):
    """
    Describes an item that can be selected or not in the settings.
    """
    def __init__(self, manager:Frame=None, name:str=None,
                 selected:bool=False, color:str="white") -> None:
        super().__init__(manager)
        self.manager = manager
        self.name = name
        self.selected = selected
        self.default_color = color
        self.configure(bg=color, width=120, height=120,
                       highlightbackground="#660000", highlightthickness=6)
        self.propagate(False)

        self.setup_container()

    def setup_container(self) -> bool:
        """
        Defines the container of the item.
        """

        self.name_label = Label(self, text=self.name)
        self.name_label.pack(side="top", padx=10, pady=10, expand=True)
        if self.selected:
            self.configure(bg="#00ff00")

        # Binds to the whole widget
        self.bind("<Button-1>", self.on_click_item)
        for children in self.winfo_children():
            children.bind("<Button-1>", self.on_click_item)

        return True

    def on_click_item(self, _event=None):
        """
        Select the item.
        Its background color changes.
        """
        custom_config = self.manager.settings_manager.gui.app.config.api_config.config_json
        if self.selected:
            for prod_type in custom_config:
                for prod in prod_type["products"]:
                    if prod["title"] == self.name:
                        prod["selected"] = False
            self.selected = False
            self.configure(bg=self.default_color, highlightbackground="#660000")
        else:
            for prod_type in custom_config:
                for prod in prod_type["products"]:
                    if prod["title"] == self.name:
                        prod["selected"] = True
            self.configure(bg="#00cc00", highlightbackground="#004400")
            self.selected = True
        self.manager.settings_manager.gui.app.config.update_custom_config(custom_config)
