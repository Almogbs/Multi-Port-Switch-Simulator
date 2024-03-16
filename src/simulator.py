import numpy as np
import sys

from common import debug_lvl, log
from constants import args
from switch import switch


if __name__ == "__main__":
    ticks = int(sys.argv[args.ARGS_TICKS.value])
    in_ports = int(sys.argv[args.ARGS_IN_PORTS.value])
    out_ports = int(sys.argv[args.ARGS_OUT_PORTS.value])

    # parse the probability matrix
    start = args.ARGS_PROB_MAT.value
    end = start + in_ports * out_ports
    prob_mat = sys.argv[start : end]
    prob_mat = np.array(prob_mat, dtype=float).reshape(in_ports, out_ports)

    # parse the lamdas for the in ports
    start = end
    end = start + in_ports
    lamdas = sys.argv[start : end]
    lamdas = np.array(lamdas, dtype=float)

    # parse the queue sizes for the out ports
    start = end
    end = start + out_ports
    queue_sizes = sys.argv[start : end]
    queue_sizes = np.array(queue_sizes, dtype=int)
    
    # parse the service rates for the out ports
    start = end
    end = start + out_ports
    service_rates = sys.argv[start : end]
    service_rates = np.array(service_rates, dtype=float)

    log("Ticks: " + str(ticks))
    log("In ports: " + str(in_ports))
    log("Out ports: " + str(out_ports))
    log("Prob mat: " + str(prob_mat))
    log("Lamdas: " + str(lamdas))
    log("Queue sizes: " + str(queue_sizes))
    log("Service rates: " + str(service_rates))

    # initialize the switch
    sw = switch(ticks, in_ports, out_ports, prob_mat, lamdas, queue_sizes, service_rates)

    # run the simulation and print the stats
    sw.run()
    sw.print_stats()
