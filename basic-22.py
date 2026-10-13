# 37. Multithreading in Python
# Multithreading allows a program to run multiple threads (small units of execution) concurrently within the same process.

# 1. Threads
# - A thread is the smallest unit of execution inside a process.
# Process → Independent program
# Thread → Lightweight task inside a process
# Threads share memory of the same process

import threading

def task():
    print("Thread is running")

t = threading.Thread(target=task)

t.start()
t.join()

print("Main thread finished")

# 2. threading Module
# - Python provides the threading module to create and manage threads.
# - Important methods:
# Method - Purpose
# start() - Starts a thread
# join() - Waits for thread completion
# is_alive() - Checks if thread is running
# current_thread() - Returns current thread
# active_count() - Number of active threads

import threading

def show():
    print(threading.current_thread().name)

t1 = threading.Thread(target=show, name="Worker-1")
t1.start()
t1.join()

# Output: Worker-1

# 3. Thread Lifecycle
# - A thread goes through several states:
# Created
#    ↓
#  Started
#    ↓
#  Running
#    ↓
#  Blocked / Waiting
#    ↓
#  Terminated

import threading
import time

def task():
    print("Running")
    time.sleep(2)
    print("Finished")

t = threading.Thread(target=task)

print("Created")
t.start()
t.join()
print("Terminated")

# 4. Locks
# - A Lock prevents multiple threads from accessing shared resources simultaneously.
# Without Lock:
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)
# Result may be incorrect due to race conditions.
# Using Lock:
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter) # 200000

# 5. RLock (Reentrant Lock)
# An RLock allows the same thread to acquire the lock multiple times.
# Lock example causing problem:
lock.acquire()
lock.acquire()  # Deadlock
# Using RLock:
import threading

lock = threading.RLock()

def task():
    with lock:
        print("First acquire")

        with lock:
            print("Second acquire")

task()
# Output:
# First acquire
# Second acquire

# 6. Semaphore
# - A Semaphore limits the number of threads that can access a resource simultaneously.
import threading
import time

sem = threading.Semaphore(2)

def worker(name):
    with sem:
        print(f"{name} working")
        time.sleep(3)
        print(f"{name} done")

for i in range(5):
    threading.Thread(
        target=worker,
        args=(f"Thread-{i}",)
    ).start()
# - Only 2 threads run at the same time.

# 7. Event
# - An Event is used for thread communication.
# - One thread waits while another thread signals.
import threading
import time

event = threading.Event()

def waiter():
    print("Waiting...")
    event.wait()
    print("Received signal")

def signaler():
    time.sleep(3)
    print("Sending signal")
    event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=signaler).start()

# Output:
# Waiting...
# Sending signal
# Received signal

# 8. Race Conditions
# - A race condition occurs when multiple threads modify shared data simultaneously.
import threading

balance = 100

def withdraw():
    global balance

    for _ in range(50):
        balance -= 1

t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=withdraw)

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
# Expected: 0
# Actual output may vary because threads interfere with each other.
# Solution:
with lock:
    balance -= 1

# 9. Thread Pools
# - Creating threads repeatedly is expensive.
# - A Thread Pool maintains a collection of reusable worker threads.
# Benefits:
# Better performance
# Less overhead
# Easier management
# Task scheduling

# 10. concurrent.futures
# - Provides high-level APIs for thread pools.
# ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])

print(list(results)) # [1, 4, 9, 16, 25]

# Using submit()
from concurrent.futures import ThreadPoolExecutor

def add(a, b):
    return a + b

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(add, 10, 20)

print(future.result()) # 30

# Threading vs Multiprocessing
# Feature - Threading - Multiprocessing
# Memory - Shared - Separate
# Speed - Fast creation - Slower creation
# Communication - Easy - More complex
# Best for - I/O-bound tasks - CPU-bound tasks
# Examples - File download, APIs - Image processing, ML

# Interview Questions
# Q1: What is a thread?
# A lightweight unit of execution within a process.

# Q2: Why use multithreading?
# To perform multiple tasks concurrently and improve responsiveness.

# Q3: What is a race condition?
# When multiple threads access shared data simultaneously leading to unpredictable results.

# Q4: What is the difference between Lock and RLock?
# Lock → can be acquired once.
# RLock → same thread can acquire multiple times.

# Q5: What is a ThreadPoolExecutor?
# A high-level interface for managing and executing tasks in a pool of worker threads.

# Quick Summary
# Thread → Lightweight execution unit.
# threading → Module for thread management.
# Lock → Prevents concurrent access.
# RLock → Reentrant lock.
# Semaphore → Limits concurrent threads.
# Event → Thread communication.
# Race Condition → Shared-data conflict.
# Thread Pool → Reusable worker threads.
# ThreadPoolExecutor → Simplified thread pool management.

# ------------------------------------------- #
# 38. Multiprocessing (Python)
# - Multiprocessing is used to run multiple processes simultaneously. It is best for CPU-bound tasks because each process has its own Python interpreter and memory space, bypassing the GIL (Global Interpreter Lock).

# 1. Processes
# - A process is an independent program execution with its own memory.
from multiprocessing import Process

def task():
    print("Child Process Running")

p = Process(target=task)

p.start()   # Start process
p.join()    # Wait for completion

print("Main Process Finished")

# Output:
# Child Process Running
# Main Process Finished

# 2. multiprocessing Module
# - Python provides the multiprocessing module to create and manage processes.
import multiprocessing

print("CPU Cores:", multiprocessing.cpu_count())

# Creating multiple processes:
from multiprocessing import Process

def square(n):
    print(n * n)

processes = []

for i in range(5):
    p = Process(target=square, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# 3. Process Pools
# - A Pool manages a group of worker processes automatically.
# map()
from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as pool:
    result = pool.map(square, [1, 2, 3, 4, 5])

print(result) # [1, 4, 9, 16, 25]

# apply()
from multiprocessing import Pool

def add(a, b):
    return a + b

with Pool(2) as pool:
    result = pool.apply(add, (5, 3))

print(result) # 8

# 4. IPC (Inter-Process Communication)
# - Processes do not share memory by default.
# - IPC allows processes to exchange data using:
# Queues
# Pipes
# Shared Memory
# Managers

# 5. Queues
# - Safe way to exchange data between processes.
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello")

q = Queue()

p = Process(target=worker, args=(q,))
p.start()

print(q.get())

p.join()

# Output: Hello

# Multiple Values
from multiprocessing import Queue, Process

def producer(q):
    for i in range(5):
        q.put(i)

q = Queue()

p = Process(target=producer, args=(q,))
p.start()

for _ in range(5):
    print(q.get())

p.join()

# 6. Pipes
# - A Pipe creates a direct connection between two processes.
from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Hello from child")
    conn.close()

parent_conn, child_conn = Pipe()

p = Process(target=sender, args=(child_conn,))
p.start()

print(parent_conn.recv())

p.join()

# Output: Hello from child

# 7. Shared Memory
# - Normally each process has separate memory.
# - Shared memory allows processes to access common data.

# Value
from multiprocessing import Process, Value

def increment(num):
    num.value += 1

number = Value('i', 10)

p = Process(target=increment, args=(number,))
p.start()
p.join()

print(number.value) # 11

# Array
from multiprocessing import Process, Array

def modify(arr):
    for i in range(len(arr)):
        arr[i] *= 2

arr = Array('i', [1, 2, 3, 4])

p = Process(target=modify, args=(arr,))
p.start()
p.join()

print(list(arr)) # [2, 4, 6, 8]

# 8. CPU-Bound Workloads
# - CPU-bound tasks spend most of their time performing calculations.
# Examples:
# Prime number calculations
# Matrix multiplication
# Image processing
# Video encoding
# Machine learning training

# Without Multiprocessing
def square_numbers():
    total = 0
    for i in range(10_000_000):
        total += i * i

square_numbers()
# Uses only one CPU core.

# With Multiprocessing
from multiprocessing import Pool

def square(n):
    return n * n

numbers = range(1000000)

with Pool() as pool:
    result = pool.map(square, numbers)
# Uses multiple CPU cores and is usually faster for heavy computations.

# Multiprocessing vs Multithreading
# Feature - Multiprocessing - Multithreading
# Unit - Process - Thread
# Memory - Separate - Shared
# GIL Impact - No - Yes
# Best For - CPU-bound tasks - I/O-bound tasks
# Communication - IPC required - Easy
# Overhead - Higher - Lower

# Interview Questions
# 1. What is multiprocessing?
# Running multiple processes simultaneously to utilize multiple CPU cores.

# 2. Why use multiprocessing instead of threading?
# For CPU-intensive tasks because it bypasses the GIL.

# 3. What is a Process Pool?
# A collection of worker processes managed automatically by Pool.

# 4. Difference between Queue and Pipe?
# Queue → Multiple producers/consumers.
# Pipe → Usually communication between two processes.

# 5. What is IPC?
# Inter-Process Communication, used to exchange data between processes.

# 6. What are CPU-bound tasks?
# Tasks that spend most of their execution time using the CPU rather than waiting for I/O.

# 7. What is shared memory?
# Memory accessible by multiple processes for data sharing.

# 8. When should multiprocessing be used?
# When tasks are computationally intensive and can run independently on multiple CPU cores.