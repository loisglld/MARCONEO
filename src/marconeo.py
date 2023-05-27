"""
marconeo.py

Defines MarcoNeo's app class.
MarcoNeo class encapsulates the whole logic of the application
as well as the connections to the database and the RFID reader.
"""

#-------------------------------------------------------------------#

from src.utils.loggers import Loggers
from src.data.member import Member
from src.data.cart import Cart
from src.data.config import Config
from src.data.db_cursor import DBCursor
from src.data.payment_service import PaymentService
from src.data.rfid import RFID
from src.interface.user_interface import GUI

#-------------------------------------------------------------------#

class MarcoNeo:
    """
    MarcoNeo's app class.
    MarcoNeo class encapsulates the whole logic of the application
    as well as the connections to the database and the RFID reader.
    """

    NAME = "MARCONEO"
    VERSION = "0.6"

    def __init__(self) -> None:
        """
        MarcoNeo's app class's constructor.
        """
        # Setup the loggers
        self.loggers = Loggers(MarcoNeo.NAME)
        self.loggers.log.info("Starting MarcoNeo v%s...", MarcoNeo.VERSION)

        # Setup the client user
        self.current_user = Member(self)
        self.cart = Cart(self.loggers, self.current_user)

        # Setup the database cursor and payment service
        self.config = Config(self)
        self.db_cursor = DBCursor(self)
        self.payment_service = PaymentService(self)

        # Setup the RFID reader and the GUI
        self.rfid = RFID(self)
        self.gui = GUI(self)

        self.loggers.log.info("MarcoNeo launched.")
        self.gui.start()

    def close(self):
        """
        Quits the application.
        """
        # Close the database connection safely
        self.db_cursor.close()
        # Close the rest of the application
        self.gui.close()
        self.loggers.log.info("Closing MARCONEO...")
        self.loggers.close()

    def update_user(self, user_data:dict) -> None:
        """
        Updates the current user.
        """
        del self.current_user
        self.current_user = Member(self, user_data)
        del self.cart
        self.cart = Cart(self.loggers, self.current_user)
        self.gui.shopping_menu.right_grid.header.member_card.update_card(self.current_user)
        self.gui.shopping_menu.right_grid.body.update_body(self.gui.shopping_menu.current_toggle)
        self.gui.shopping_menu.right_grid.footer.update_footer()
