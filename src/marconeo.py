"""
marconeo.py

Defines MarcoNeo's app class.
MarcoNeo class encapsulates the whole logic of the application
as well as the connections to the database and the RFID reader.
"""

#-------------------------------------------------------------------#

from src.utils.loggers import Loggers
from src.data.cart import Cart
from src.data.config import Config
from src.data.database import DBCursor
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
    RELEASE_DATE = None

    def __init__(self) -> None:
        """
        MarcoNeo's app class's constructor.
        """
        # Setup the logger
        self.loggers = Loggers(MarcoNeo.NAME)
        self.loggers.log.info("Starting MarcoNeo v%s...", MarcoNeo.VERSION)

        # Setup the current user
        self.current_user = None
        self.cart = Cart(self.loggers, self.current_user)

        self.config = Config(self)
        self.db_cursor = DBCursor(self)
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

    def update_user(self, user):
        """
        Updates the current user.
        """
        self.current_user = user
        self.cart.__init__(self.loggers, self.current_user)
        self.gui.shopping_menu.right_grid.body.update_body(self.gui.shopping_menu.current_toggle)
        self.gui.shopping_menu.right_grid.footer.update_footer()

    def confirm_purchase(self):
        """
        Confirms the purchase.
        """
        if self.current_user is None:
            self.loggers.log.warning("No user is logged in. Can't purchase.")
            return
        self.current_user.balance -= self.cart.total
        self.db_cursor.update_balance(self.current_user)
        self.loggers.log.info("Purchase confirmed. New balance of %s is %s€.",
                              self.current_user.first_name, self.current_user.balance)
        print(f"Purchase confirmed. Your new balance is {self.current_user.balance}€.")
