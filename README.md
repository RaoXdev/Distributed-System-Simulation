# Distributed-System-Simulation

A Python-based simulation of a distributed system using asynchronous programming with asyncio. The system simulates task assignments and worker specialization, with the inclusion of network delays, message queues, and task monitoring.

Features
Asynchronous Task Assignment: Tasks are dynamically assigned to workers based on their specialization.

Worker Specialization: Workers are specialized to handle specific types of tasks (e.g., Type-1, Type-2, Type-3).

Network Simulation: Introduces random network delays to simulate real-world latency.

Task Monitoring: Monitors the completion of tasks and logs the results.

Real-Time Output: Uses the rich library to display real-time interactive outputs during task processing.

Logging: All task completions are logged to a file for further analysis.

Distributed-System-Simulation/
├── network/          # Network-related modules for message passing
├── nodes/            # Contains classes for the Manager and Workers
├── test/             # Test cases for the simulation
├── main.py           # Main entry point for the simulation
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

This project requires Python 3.7+ and the following dependencies:
asyncio: For asynchronous programming
rich: For colorful and interactive terminal output.

You can install the required dependencies using pip:
`pip install -r requirements.txt`

Install the dependencies:
`pip install -r requirements.txt`

To run the simulation, execute the main.py script:
`python main.py`
