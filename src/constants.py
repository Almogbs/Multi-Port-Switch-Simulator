# Description: This file contains constants for the simulator.

from enum import Enum

class args(Enum):
    """
    Enumeration class representing the arguments for the simulator.
    
    Attributes:
        ARGS_TICKS (int): The number of ticks for the simulation.
        ARGS_IN_PORTS (int): The number of input ports.
        ARGS_OUT_PORTS (int): The number of output ports.
        ARGS_PROB_MAT (int): The probability matrix for the simulation.
    """
    ARGS_TICKS = 1
    ARGS_IN_PORTS = 2
    ARGS_OUT_PORTS = 3
    ARGS_PROB_MAT = 4
