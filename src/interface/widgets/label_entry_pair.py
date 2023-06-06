"""
label_entry_pair.py

Contains the LabelEntryPair widget
which is a Label and an Entry.
"""

#-------------------------------------------------------------------#

from src.utils.gui_utils import Frame, Label, Entry

#-------------------------------------------------------------------#

class LabelEntryPair(Frame):
    """
    Templates containing a label and an entry.
    """
    def __init__(self, master=None, text:str="", entry_text:str="", **kwargs) -> None:
        Frame.__init__(self, master, **kwargs)
        self.configure(bg="#FFFFFF")
        self.label = Label(self, text=text+":", bg="#FFFFFF", fg="#000000")
        self.entry = Entry(self, text=entry_text, bg="#FFFFFF", fg="#000000")
        self.label.pack(side='left', padx=10, pady=10)
        self.entry.pack(side='left', padx=10, pady=10)

        self.label.bind("<Button-1>", self.on_label_click)


    def on_label_click(self, _event):
        """
        Prints the text of the label.
        """
        print(self.label['text'])
