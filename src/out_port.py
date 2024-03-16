# Description: This file contains the out_port class which represents an output port in a simulator.

import numpy as np

from common import log, debug_lvl
from packet import packet


class out_port:
    """
    Represents an output port in a simulator.

    Attributes:
        port_id (int): The ID of the port.
        queue_size (int): The maximum size of the queue.
        service_rate (int): The rate at which packets are serviced.
        queue (list): The queue of packets waiting to be serviced.
        succ_packets (int): The number of successfully serviced packets.
        dropped_packets (int): The number of dropped packets due to queue overflow.

    Methods:
        __init__(self, port_id: int, queue_size: int, service_rate: int) -> None:
            Initializes a new instance of the out_port class.
        __str__(self) -> str:
            Returns a string representation of the out_port object.
        add_packet(self, packet: packet) -> bool:
            Adds a packet to the queue.
        service_packets(self, current_time: int) -> None:
            Services the packets in the queue.
    """
    def __init__(self, port_id: int, queue_size: int, service_rate: int) -> None:
        self.port_id = port_id
        self.queue_size = queue_size
        self.service_rate = service_rate
        self.queue = []
        self.succ_packets = 0
        self.dropped_packets = 0
    
    def __str__(self) -> str:
        return f"Port id: {self.port_id} Queue size: {self.queue_size} Service rate: {self.service_rate} \
                 Queue: {self.queue} Succ packets: {self.succ_packets} Dropped packets: {self.dropped_packets}"
    
    def add_packet(self, packet: packet) -> bool:
        """
        Adds a packet to the queue.
        
        Args:
            packet (packet): The packet to be added to the queue.
        
        Returns:
            bool: True if the packet was successfully added to the queue, False otherwise.
        """
        if len(self.queue) < self.queue_size:
            self.queue.append(packet)
            self.succ_packets += 1
            return True
        else:
            self.dropped_packets += 1
            return False
    
    def service_packets(self, current_time: int) -> None:
        """
        Services the packets in the queue.

        Args:
            current_time (int): The current time in the simulation.
        """
        if len(self.queue) > 0:
            packets_to_service = np.random.poisson(self.service_rate)
            service_rate = packets_to_service
            log(f"Tick: {current_time}, Out port: {self.port_id}, Pending Packets: {len(self.queue)}, To Serve: {packets_to_service}",
                debug_lvl.DEBUG_LVL_FML.value)

            while packets_to_service > 0 and len(self.queue) > 0:
                packet = self.queue.pop(0)
                packet.service_time = current_time
                packet.service_rate = (1 / service_rate)
                packets_to_service -= 1
