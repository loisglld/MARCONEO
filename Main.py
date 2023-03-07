"""
Main.py

Entrypoint of the application.
It launches the application.
"""

#------------------------------------------------------------------------------#

from MarcoNeo import MarcoNeo

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    print("Starting MarcoNeo...")
    marco = MarcoNeo()
    marco.start()
    marco.quit()
    print("MarcoNeo stopped.")