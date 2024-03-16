# Description: A class representing a switch in a simulation.

import numpy as np

from common import log, debug_lvl
from out_port import out_port
from packet import packet

class switch:
    """
    A class representing a switch in a network simulation.

    Attributes:
    - ticks (int): The number of simulation ticks.
    - in_ports_num (int): The number of input ports.
    - out_ports_num (int): The number of output ports.
    - prob_mat (np.ndarray): The probability matrix for packet routing.
    - lamdas (np.ndarray): The arrival rates for each input port.
    - queue_sizes (np.ndarray): The maximum queue sizes for each output port.
    - service_rates (np.ndarray): The service rates for each output port.
    - packets (list): The list of packets in the switch.
    - out_ports (list): The list of output ports in the switch.
    - dropped_packets (int): The number of dropped packets.
    - succ_packets (int): The number of successfully transmitted packets.
    - current_time (int): The current simulation time.
    - start (bool): Indicates whether the simulation has started.

    Methods:
    - __init__(self, ticks: int, in_ports_num: int, out_ports_num: int,
               prob_mat: np.ndarray, lamdas: np.ndarray, queue_sizes: np.ndarray,
               service_rates: np.ndarray) -> None:
        Initializes a switch object with the given parameters.

    - __str__(self) -> str:
        Returns a string representation of the switch.

    - pending_packets(self) -> bool:
        Checks if there are any pending packets in the switch.

    - run(self) -> None:
        Runs the simulation.

    - print_stats(self) -> None:
        Prints the statistics of the simulation.
    """
    def __init__(self, ticks: int, in_ports_num: int, out_ports_num: int,
                 prob_mat: np.ndarray, lamdas: np.ndarray, queue_sizes: np.ndarray,
                 service_rates: np.ndarray) -> None:
        self.ticks = ticks
        self.in_ports_num = in_ports_num
        self.out_ports_num = out_ports_num
        self.prob_mat = prob_mat
        self.lamdas = lamdas
        self.queue_sizes = queue_sizes
        self.service_rates = service_rates
        self.packets = []
        self.out_ports = []
        self.dropped_packets = 0
        self.succ_packets = 0
        self.current_time = 0
        self.start = False
        
        for i in range(out_ports_num):
            self.out_ports.append(out_port(i, queue_sizes[i], service_rates[i]))

    def __str__(self) -> str:
        return f"Ticks: {self.ticks} In ports num: {self.in_ports_num} Out ports num: {self.out_ports_num} \
                 Prob mat: {self.prob_mat} Lamdas: {self.lamdas} Queue sizes: {self.queue_sizes} \
                 Service rates: {self.service_rates} Packets: {self.packets} Out ports: {self.out_ports} \
                 Dropped packets: {self.dropped_packets} Succ packets: {self.succ_packets} \
                 Current time: {self.current_time} Start: {self.start}"

    def pending_packets(self) -> bool:
        """
        Checks if there are any pending packets in the out ports' queues.

        Returns:
            bool: True if there are pending packets, False otherwise.
        """
        for out_port in self.out_ports:
            if len(out_port.queue) > 0:
                return True
        
        return False

    def run(self) -> None:
        """
        Runs the simulation for a specified number of ticks.

        The simulation generates packets based on the arrival rates for each input port,
        and routes them to the output ports based on the probability matrix. It keeps track
        of successful packets and dropped packets.
        """
        self.start = True

        # We want to keep serving as long as the simulator has not reached the end of the ticks or there are pending packets
        while self.current_time < self.ticks or self.pending_packets():
            for out_port in self.out_ports:
                # Re-initialize the out port for the new tick (setting the new rates etc), pending packets won't be flushed
                out_port.tick_start(self.current_time)
                # Edge case: if the last tick ended and the queues are full, we need to serve the packets before the new tick,
                # ow, new packets won't be added to the queue
                out_port.serve_packets()
            
            # Only if we are not at the end of the ticks, we can generate new packets
            if self.current_time < self.ticks:
                for in_port in range(self.in_ports_num):
                    num_packets = np.random.poisson(self.lamdas[in_port])

                    log(f"Tick: {self.current_time}, In port: {in_port}, New packets: {num_packets}",
                        debug_lvl.DEBUG_LVL_FML.value)

                    for _ in range(num_packets):
                        out_port = np.random.choice(self.out_ports_num, 1, p=self.prob_mat[in_port])[0]
                        p = packet(self.current_time, in_port, out_port)
                        self.packets.append(p)
                        ret = self.out_ports[out_port].add_packet(p)
                        if ret:
                            self.succ_packets += 1
                        else:
                            self.dropped_packets += 1
            
            # Before the new tick, we serve the packets in the out ports.
            # Proboably not nessesary, as we already served the packets in the out ports in the first loop
            for out_port in range(self.out_ports_num):
                self.out_ports[out_port].serve_packets()
            
            self.current_time += 1
            
    def print_stats(self) -> None:
        """
        Prints the statistics of the simulation.

        The statistics include the number of successful packets sent,
        the number of successful packets sent through each output port,
        the number of dropped packets,
        the number of dropped packets through each output port,
        the current time of the simulation,
        the average waiting time of successful packets,
        and the average service time of successful packets.

        If the simulation has not been started, it prints a message indicating
        that the simulation has not started.
        """
        if not self.start:
            log("Simulation not started")
            return
        
        stats = []
        stats.append(self.succ_packets)

        for out_port in self.out_ports:
            stats.append(out_port.succ_packets)

        stats.append(self.dropped_packets)

        for out_port in self.out_ports:
            stats.append(out_port.dropped_packets)

        # maybe -1 ?
        stats.append(self.current_time)

        avg_waiting_time = 0
        avg_service_time = 0
        cntr = 0
        for packet in self.packets:
            if packet.dropped():
                continue

            avg_waiting_time += packet.service_time - packet.arrival_time
            avg_service_time += packet.service_rate
            cntr += 1
        
        avg_waiting_time /= cntr
        avg_service_time /= cntr

        stats.append(avg_waiting_time)
        stats.append(avg_service_time)

        print(" ".join(map(str, stats)))
