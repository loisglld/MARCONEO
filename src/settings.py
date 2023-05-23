"""
settings.py

Contains the settings stats of the application.
"""

#-------------------------------------------------------------------#

from dataclasses import dataclass

#-------------------------------------------------------------------#

@dataclass
class SettingsStats:
    """
    Contains the settings stats of the application.
    """
    dark_mode: bool = True
    language: str = "en"
