"""
label_label_pair.py

Contains the LabelLabelPair widget
which is a Label and an Entry.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label

#-------------------------------------------------------------------#

class LabelLabelPair(Frame):
    """
    Templates containing two labels.
    """
    def __init__(self, master=None, name:str="", price:str="", **kwargs) -> None:
        Frame.__init__(self, master, **kwargs)
        self.configure(bg="#898989")
        self.name = name
        self.price = price
        self.focused = False
        self.label = Label(self, text=self.name+":", bg="#FFFFFF", fg="#000000")
        self.entry = Label(self, text=self.price, bg="#FFFFFF", fg="#000000")
        self.label.pack(side='left', padx=10, pady=10)
        self.entry.pack(side='left', padx=10, pady=10)

        # Bindings to cover the whole widget
        self.bind("<Button-1>", self.on_label_click)
        self.label.bind("<Button-1>", self.on_label_click)
        self.entry.bind("<Button-1>", self.on_label_click)

    def on_label_click(self, _event):
        """
        Prints the text of the label.
        """
        for widget in self.master.winfo_children():
            widget.focused = False
            widget.configure(bg="#898989")

        self.focused = True

        self.config(bg="#dedede")
