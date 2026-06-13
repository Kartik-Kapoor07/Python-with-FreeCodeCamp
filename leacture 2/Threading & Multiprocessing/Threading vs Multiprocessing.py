"""
=========================================
THREADING VS MULTIPROCESSING IN PYTHON
=========================================

Goal:
-----
Understand the difference between Threading and Multiprocessing,
when to use each one, and how they utilize system resources.

---------------------------------------------------------------
WHAT IS A PROCESS?
---------------------------------------------------------------

A process is a running program.

Examples:
- Chrome running
- VS Code running
- Spotify running
- A Python script running

Each process has:
- Its own memory
- Its own resources
- Its own variables
- Its own files

Processes are isolated from each other.

Example:

Process A
    balance = 1000

Process B
    Cannot directly access balance

---------------------------------------------------------------
WHAT IS A THREAD?
---------------------------------------------------------------

A thread is a worker inside a process.

A process can contain one or more threads.

Example:

Python Process
├── Main Thread
├── Thread 1
├── Thread 2
└── Thread 3

Threads share the same memory of the process.

---------------------------------------------------------------
WHY USE THREADING?
---------------------------------------------------------------

Threading is useful when the program spends most of its time
waiting for something.

Examples:
- Downloading files
- API requests
- Web scraping
- Database queries
- Chat applications
- Reading network data

These are called I/O-bound tasks.

I/O = Input / Output

The CPU spends most of its time waiting rather than calculating.

---------------------------------------------------------------
WHY USE MULTIPROCESSING?
---------------------------------------------------------------

Multiprocessing is useful when the CPU spends most of its time
performing calculations.

Examples:
- Machine Learning
- Data Analysis
- Image Processing
- Video Processing
- Scientific Simulations
- Backtesting Trading Strategies

These are called CPU-bound tasks.

The CPU is busy performing calculations rather than waiting.

---------------------------------------------------------------
THREADING VS MULTIPROCESSING
---------------------------------------------------------------

THREADING
----------
✓ Multiple threads inside one process
✓ Shared memory
✓ Lightweight
✓ Fast communication between threads
✓ Best for I/O-bound tasks

MULTIPROCESSING
---------------
✓ Multiple independent processes
✓ Separate memory
✓ Better CPU utilization
✓ Can use multiple CPU cores
✓ Best for CPU-bound tasks

---------------------------------------------------------------
IMPORTANT RULE
---------------------------------------------------------------

If the program spends most of its time:

Waiting  -> Use Threading

Calculating -> Use Multiprocessing

---------------------------------------------------------------
TOPICS TO LEARN NEXT
---------------------------------------------------------------

1. Creating Threads
2. Thread.start()
3. Thread.join()
4. Creating Processes
5. Process.start()
6. Process.join()
7. Shared Memory
8. Race Conditions
9. Locks
10. Queues
11. GIL (Global Interpreter Lock)

---------------------------------------------------------------
NOTES
---------------------------------------------------------------

My CPU:
- Intel Core i5-12400F
- 6 Physical Cores
- 12 Hardware Threads

A program can create many software threads, but the operating
system schedules them onto the available hardware threads.like im my
case there are total 12 threads and in anycase if i give 100 threads
work and i will provide all the info about which work will handeled by
which thread so after threads do there first task the will move to 
second one

just like waiter in a overloaded restaurants
"""

from multiprocessing import Process
import time

def work():
    print("Started")
    time.sleep(3)
    print("Finished")

if __name__ == "__main__":
    p1 = Process(target=work)
    p2 = Process(target=work)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

print("Done")