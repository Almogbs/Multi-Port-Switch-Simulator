# Multi-Port-Switch-Simulator

This project is a multi-port switch simulator that allows you to simulate the behavior of a network switch with multiple ports. It provides a flexible and customizable environment for testing and experimenting with network configurations.

## Installation

To install and run the multi-port switch simulator, follow these steps:

1. Clone the repository: `git clone https://github.com/almogbs/Multi-Port-Switch-Simulator.git`
2. Navigate to the project directory: `cd Multi-Port-Switch-Simulator`
3. Requirements: This project requires Python 3.6 or later. Install the req packages using pip:

```bash
pip install -r requirements.txt

## Usage
```bash
./simulator T N M 𝑃0,0 𝑃0,1…𝑃0,𝑀−1 𝑃1,0 𝑃1,1…𝑃1,𝑀−1 … 𝑃𝑁−1,0 𝑃𝑁−1,1 … 𝑃𝑁−1,𝑀−1 𝜆0 𝜆1 … 𝜆𝑁−1 𝑄0 𝑄1… 𝑄𝑀−1 𝜇0 𝜇1 … 𝜇𝑀−1

Where:
- T: Time units for the simulation
- N: Number of Input Ports
- M: Number of Output Ports
- 𝑃0,0 𝑃0,1 … 𝑃0,𝑀−1 𝑃1,0 𝑃1,1 … 𝑃1,𝑀−1 … 𝑃𝑁−1,0 𝑃𝑁−1,1 … 𝑃𝑁−1,𝑀−1: Probability matrix that mapped between input and output ports
- 𝜆0 𝜆1 … 𝜆𝑁−1: Poisson parameters for the input packets arrival rate
- 𝑄0 𝑄1 … 𝑄𝑀−1: Sizes for the output ports queues
- 𝜇0 𝜇1 … 𝜇𝑀−1: Poisson parameters for the output ports service rate
