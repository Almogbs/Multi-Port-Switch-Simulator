# Description: This file contains the packet class which represents a packet in a switch simulation.

class packet:
    """
    Represents a packet in a network simulation.

    Attributes:
        arrival_time (int): The arrival time of the packet.
        service_time (int): The service time of the packet.
        service_rate (int): The service rate of the packet.
        in_port_idx (int): The index of the input port for the packet.
        out_port_idx (int): The index of the output port for the packet.

    Methods:
        __init__(self, arrival_time: int, in_port_idx: int, out_port_idx: int) -> None:
            Initializes a new instance of the packet class.
        __str__(self) -> str:
            Returns a string representation of the packet object.
        dropped(self) -> bool:
            Checks if the packet has been dropped.
    """

    def __init__(self, arrival_time: int, in_port_idx: int, out_port_idx: int) -> None:
        self.arrival_time = arrival_time
        self.service_time = -1
        self.service_rate = -1
        self.in_port_idx = in_port_idx
        self.out_port_idx = out_port_idx

    def __str__(self) -> str:
        return f"Arrival time: {self.arrival_time} Service time: {self.service_time} \
                 Service rate: {self.service_rate} In port idx: {self.in_port_idx} \
                 Out port idx: {self.out_port_idx} Dropped: {self.dropped()}"

    def dropped(self) -> bool:
        """
        Checks if the packet has been dropped.

        Returns:
            bool: True if the packet has been dropped, False otherwise.
        """
        return self.service_time == -1
