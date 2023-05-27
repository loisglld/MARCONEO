"""
logins.py

This module contains the Logins class.
Contains the logins to connect to the database.
"""

#------------------------------------------------------------------------------#

from dataclasses import dataclass

#------------------------------------------------------------------------------#

@dataclass
class Logins:
    """
    Logins class.
    Contains the logins to connect to the database.
    """
    _host: str = "host"
    _database: str = "marconeo"
    _user: str = "root"
    _password: str = "password"
    _port: int = 3306

    def __init__(self) -> None:
        """
        Logins constructor.
        """
        with open("./pwd.txt", "r", encoding="utf-8") as logins_file:
            self._host = logins_file.readline().strip()
            self._database = logins_file.readline().strip()
            self._user = logins_file.readline().strip()
            self._password = logins_file.readline().strip()
            self._port = int(logins_file.readline().strip())

    def get_host(self) -> str:
        """
        Returns the host.
        """
        return self._host

    def get_database(self) -> str:
        """
        Returns the database.
        """
        return self._database

    def get_user(self) -> str:
        """
        Returns the user.
        """
        return self._user

    def get_password(self) -> str:
        """
        Returns the password.
        """
        return self._password

    def get_port(self) -> int:
        """
        Returns the port.
        """
        return self._port
