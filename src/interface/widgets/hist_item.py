"""
hist_item.py

Defines the HistoryItem class.
"""

#-------------------------------------------------------------------#

import datetime
from src.utils.gui_utils import Label, Frame

#-------------------------------------------------------------------#

class HistoryItem(Frame):
    """
    Item in which is displayed an order from the history.
    """
    def __init__(self, manager, item_purchased) -> None:
        super().__init__(manager)
        self.member_name = item_purchased[0]
        self.item_name = item_purchased[1]
        self.price = item_purchased[2]
        self.amount = item_purchased[3]
        self.date = item_purchased[4].strftime("%d/%m/%Y %H:%M")
        self.config(bg="#333333")
        self.setup_label()

    def setup_label(self) -> None:
        """
        Defines the labels used in the history item.
        """
        Label(self, text=f"{self.member_name}").pack(side="left", padx=10)
        Label(self, text=f"-{self.price}€").pack(side="left", padx=10)

        date_label = Label(self, text=f"{self.get_day_description(self.date)}")
        date_label.pack(side="left", padx=10, expand=True, fill='x')
        date_label.configure(anchor="center")

        Label(self, text=f"{self.amount}x{self.item_name}").pack(side="right", padx=10)


    def get_day_description(self, date:datetime.datetime):
        """
        Returns a description of the date given.
        """
        formated_date = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M")
        now = datetime.datetime.now().date()
        diff = now - formated_date.date()
        if diff.days == 0:
            return f"Aujourd'hui {formated_date.strftime('%H:%M')}"
        if diff.days == 1:
            return f"Hier {formated_date.strftime('%H:%M')}"
        if diff.days == 2:
            return f"Avant-hier {formated_date.strftime('%H:%M')}"
        return date
