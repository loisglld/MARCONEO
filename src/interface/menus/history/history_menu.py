"""
history_menu.py

Configure MarcoNeo's history page.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Label, AppButton, Frame
from src.interface.widgets.hist_item import HistoryItem

#-------------------------------------------------------------------#

class HistoryMenu(Frame):
    """
    MarcoNeo's history page.
    """
    MAX_HISTORY = 10
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui
        self.config(bg="#333333")
        self.setup_label()
        self.setup_buttons()
        self.history_frame = Frame(self, bg="#555555")
        self.history_frame.pack(side="top", pady=5, padx=10, fill="x")

    def setup_label(self) -> None:
        """
        Defines the labels used in the history menu.
        """
        Label(self, text="History menu",
              font="System").pack(side="top",
                                    pady=10, padx=10, fill="x")

    def setup_buttons(self) -> bool:
        """
        Defines the buttons used in the history menu.
        """
        bottom_widget = Frame(self, bg="#333333")
        self.back_btn = AppButton(bottom_widget, text="Back",
                                  command=lambda: self.gui.change_menu(self.gui.main_menu))
        self.refresh_btn = AppButton(bottom_widget, text="Refresh",
                                        command=self.refresh_history)
        self.back_btn.pack(side="left", pady=10, padx=10, fill="x", expand=True)
        self.refresh_btn.pack(side="left", pady=10, padx=10, fill="x", expand=True)
        bottom_widget.pack(side="bottom", fill="x")
        return True

    def setup_history(self) -> None:
        """
        Defines the history used in the history menu.
        """
        history = self.gui.app.db_cursor.get_history()
        for item_purchased in history:
            HistoryItem(self.history_frame,
                        item_purchased).pack(side="top",
                                             pady=7, padx=10,
                                             anchor="w",
                                             fill="x")

    def refresh_history(self):
        """
        Refesh history on the page
        """
        self.clear_history()
        self.setup_history()
        self.gui.app.loggers.log.info("History have been refreshed.")

    def clear_history(self):
        """
        Clear history on the page
        """
        for widget in self.history_frame.winfo_children():
            widget.destroy()
