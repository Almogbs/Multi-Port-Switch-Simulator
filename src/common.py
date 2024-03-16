# Description: This file contains the common definitions and functions used by the simulator.

from enum import Enum

class debug_lvl(Enum):
    """
    Enumeration class representing the debug levels for the simulator.

    Attributes:

        DEBUG_LVL_OFF (int): The debug level is off
        DEBUG_LVL_STD (int): The debug level is standard
        DEBUG_LVL_FML (int): Relly hope we don't have to use this
    """
    DEBUG_LVL_OFF= 0
    DEBUG_LVL_STD = 1
    DEBUG_LVL_FML = 2

# Set the debug level
DEBUG = debug_lvl.DEBUG_LVL_FML.value

def log(msg: str, level: int = debug_lvl.DEBUG_LVL_STD.value) -> None:
    """
    Logs a message to the console if the debug level is greater than or equal to the specified level.

    """
    if DEBUG >= level:
        print(msg)