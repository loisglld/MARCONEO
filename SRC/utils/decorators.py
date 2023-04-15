"""
decorators.py

Defines the decorators used in the application.
"""

#-------------------------------------------------------------------#

import functools
import sys

#-------------------------------------------------------------------#

def close_service(func):
    """
    Close the connection of the service when its closing method is done.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__
        attempt = 1
        while attempt <= 5:
            print(f"Closing connection of {class_name} (attempt {attempt})...")
            if result := func(*args, **kwargs):
                return result
            attempt += 1
        print("Failed to close connection")
        return None
    return wrapper

def launch_service(func):
    """
    Connect to the service when its connecting method is done.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__
        attempt = 1
        while attempt <= 5:
            print(f"Launching {class_name} (attempt {attempt})...")
            if result := func(*args, **kwargs):
                return result
            attempt += 1
        print(f"Unable to connect to {class_name}.")
        sys.exit(1)
    return wrapper

def log(func):
    """
    Log the function call.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__
        print(f"{class_name}.{func.__name__}() called.")
        return func(*args, **kwargs)
    return wrapper
