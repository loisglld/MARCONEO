"""
rfid.py

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

    def rfid_callback(self, event) -> None:
        """
        Callback function for the RFID reader.
        """
        # If the user presses the enter key (or keypad enter key), the buffer is parsed
        if event.keysym == 'Return' or event.keysym == 'KP_Enter':
            if self.buffer == "":
                return # If the buffer is empty, do nothing

            self.loggers.log.debug(f"Parsing RFID card number {self.buffer}...")
            try:
                id_in_buffer = int(self.buffer)
            except ValueError:
                self.loggers.log.error("RFID card corrupted.")
                self.buffer = "" # Reset the buffer
                self.app.update_user(None)
                return
            self.app.update_user(self.app.db.get_member(id_in_buffer))

            self.buffer = "" # Reset the buffer

        else:
            self.buffer += event.char
