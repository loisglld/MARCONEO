"""
RFID.py

This file is responsible for the RFID reader.
It is located inside the interface folder because
it is only used by the GUI: MarcoNeo app uses the
binding tkinter method to listen to the RFID reader.
"""

#------------------------------------------------------------#

class RFID:
    def __init__(self, loggers, event=None):
        self.loggers = loggers
        self.current_user_id = None
        self.buffer = ""
        
    def rfid_callback(self, event):
        # If the user presses the enter key (or keypad enter key), the buffer is parsed
        if event.keysym == 'Return' or event.keysym == 'KP_Enter':
            self.loggers.log.info(f"Parsing RFID card number {self.buffer}...")
            try:
                id = int(self.buffer)
            except Exception:
                self.loggers.log.warn(f"Failed to parse RFID card number {self.buffer}...")
            else:
                self.set_current_user_id(id)
            finally:
                self.buffer = ""
        else:
            self.buffer += event.char
    
    def set_current_user_id(self, id):
        self.current_user_id = id
