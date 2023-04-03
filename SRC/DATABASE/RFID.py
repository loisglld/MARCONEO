"""
RFID.py

This file is responsible for the RFID reader.
MarcoNeo app uses the binding tkinter method 
to listen to the RFID reader.
"""

#------------------------------------------------------------#

class RFID:
    """
    Defines the RFID reader.
    """
    def __init__(self, app):
        """
        Constructor of the RFID class.
        """
        self.app = app
        self.loggers = self.app.loggers
        self.current_user_id = None
        self.buffer = ""
        
    def rfid_callback(self, event):
        # If the user presses the enter key (or keypad enter key), the buffer is parsed
        if event.keysym == 'Return' or event.keysym == 'KP_Enter':
            if self.buffer == "": return # If the buffer is empty, do nothing
                
            self.loggers.log.debug(f"Parsing RFID card number {self.buffer}...")
            id = int(self.buffer)
            self.app.update_user(self.app.db.get_member(id))
            self.buffer = "" # Reset the buffer
        else:
            self.buffer += event.char
