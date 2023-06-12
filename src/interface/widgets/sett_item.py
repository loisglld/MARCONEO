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
                 selected:bool=False, color:str="gold") -> None:
        super().__init__(manager)
        self.manager = manager
        self.name = name
        self.selected = selected
        self.default_color = color
        self.configure(bg=color)
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
        print("selected before click: ", self.selected)
        custom_config = self.manager.settings_manager.gui.app.config.custom_config
        if self.selected:
            for prod_type in custom_config:
                for prod in prod_type["products"]:
                    if prod["name"] == self.name:
                        prod["selected"] = False
            self.selected = False
            self.configure(bg=self.default_color)
        else:
            for prod_type in custom_config:
                for prod in prod_type["products"]:
                    if prod["name"] == self.name:
                        prod["selected"] = True
            self.configure(bg="#00cc00")
            self.selected = True

        data_custom = {"data": custom_config}
        self.manager.settings_manager.gui.app.config.generate_json("custom", data_custom)
