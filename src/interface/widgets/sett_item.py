"""
sett_item.py

Item of the settings page of the app.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class SettItem:
    """
    Describes an item that can be selected or not in the settings.
    """
    def __init__(self, manager:Frame=None, name:str=None) -> None:
        self.manager = manager
        self.name = name
        self.selected = False

        self.setup_container()

    def setup_container(self) -> bool:
        """
        Defines the container of the item.
        """
        self.container = Frame(self.manager)
        self.container.configure(bg="#333333")

        self.name_label = Label(self.container, text=self.name)
        self.name_label.pack(side="top", padx=10, pady=5, fill="both", expand=True)

        # Binds to the whole widget
        self.container.bind("<Button-1>", self.on_click_item)
        for children in self.container.winfo_children():
            children.bind("<Button-1>", self.on_click_item)

        return True

    def on_click_item(self, _event=None):
        """
        Select the item.
        Its background color changes.
        """
        if self.selected:
            self.selected = False
            self.container.configure(bg="#333333")
        else:
            self.selected = True
            self.container.configure(bg="#00ff00")
