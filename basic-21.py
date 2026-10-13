# 36. Asynchronous Programming in Python
#
# Asynchronous programming allows a program to perform multiple tasks seemingly at the same time without waiting for one task to finish before starting another.

# 1. Synchronous vs Asynchronous
# Synchronous Programming
# Tasks execute one after another.
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")

task1()
task2()

# Output
# Task 1 started
# (wait 2 sec)
# Task 1 completed
# Task 2 started
# (wait 2 sec)
# Task 2 completed
# Total time ≈ 4 seconds

# Asynchronous Programming
# - Tasks can run concurrently while waiting for I/O operations.
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Output
# Task 1 started
# Task 2 started
# (wait 2 sec)
# Task 1 completed
# Task 2 completed
# Total time ≈ 2 seconds

# 2. Blocking vs Non-Blocking
# Blocking: Operation stops entire program until completed.
import time

print("Start")
time.sleep(3)
print("End")

# Non-Blocking: Program can perform other work while waiting.
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(3)
    print("End")

asyncio.run(main())

# 3. async - Used to define an asynchronous function (coroutine).
async def greet():
    print("Hello")
# - Calling it doesn't execute immediately:
greet()
# Returns: <coroutine object greet at 0x...>
# To run:
asyncio.run(greet())

# 4. await: Used inside async functions.
# - Pauses current coroutine and gives control back to event loop.
import asyncio

async def main():
    print("Before")
    await asyncio.sleep(2)
    print("After")

asyncio.run(main())
# Output:
# Before
# After
# (with 2-second delay)

# 5. asyncio
# - Python's built-in asynchronous framework.
# Features:
# Event loop
# Coroutines
# Tasks
# Futures
# Networking
# Synchronization primitives
import asyncio

async def hello():
    print("Hello Asyncio")

asyncio.run(hello())

# 6. Coroutines
# - A coroutine is an async function that can pause and resume execution.
async def fetch_data():
    await asyncio.sleep(1)
    return "Data"
# Using coroutine:
async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
# Output: Data

# 7. Tasks
# - Tasks wrap coroutines and schedule them to run concurrently.
import asyncio

async def worker(name):
    await asyncio.sleep(2)
    print(name)

async def main():
    task1 = asyncio.create_task(worker("A"))
    task2 = asyncio.create_task(worker("B"))

    await task1
    await task2

asyncio.run(main())

# Output:
# A
# B
# (after about 2 seconds)

# Multiple Tasks
import asyncio

async def job(n):
    await asyncio.sleep(n)
    print(f"Finished {n}")

async def main():
    tasks = [
        asyncio.create_task(job(1)),
        asyncio.create_task(job(2)),
        asyncio.create_task(job(3))
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())

# 8. Futures
# - A Future represents a value that will become available later.
import asyncio

async def main():
    loop = asyncio.get_running_loop()

    future = loop.create_future()

    future.set_result("Completed")

    result = await future

    print(result)

asyncio.run(main())

# output: Completed

# Difference Between Task and Future
# Future
# Placeholder for result
# Low-level object
future = loop.create_future()
# Task
# Executes coroutine
# Subclass of Future
task = asyncio.create_task(my_coroutine())

# 9. Async HTTP
# Install package: pip install aiohttp
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    html = await fetch("https://example.com")
    print(html[:100])

asyncio.run(main())

# Multiple HTTP Requests
import aiohttp
import asyncio

urls = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]

        results = await asyncio.gather(*tasks)

        for result in results:
            print(len(result))

asyncio.run(main())

# 10. Async Database Operations
# - SQLite with aiosqlite
# Install: pip install aiosqlite
# Insert Data:
import aiosqlite
import asyncio

async def main():
    async with aiosqlite.connect("test.db") as db:

        await db.execute(
            "CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT)"
        )

        await db.execute(
            "INSERT INTO users VALUES(1, 'Aman')"
        )

        await db.commit()

asyncio.run(main())

# Read Data
import aiosqlite
import asyncio

async def main():
    async with aiosqlite.connect("test.db") as db:

        async with db.execute(
            "SELECT * FROM users"
        ) as cursor:

            rows = await cursor.fetchall()

            print(rows)

asyncio.run(main())
# Output: [(1, 'Aman')]

# 11. Concurrency
# - Concurrency means handling multiple tasks during overlapping time periods.
# - It does NOT necessarily mean parallel execution.
import asyncio

async def task(name, sec):
    print(f"{name} started")

    await asyncio.sleep(sec)

    print(f"{name} completed")

async def main():

    await asyncio.gather(
        task("A", 3),
        task("B", 2),
        task("C", 1)
    )

asyncio.run(main())

# Output:
# A started
# B started
# C started
#
# C completed
# B completed
# A completed
# Total time ≈ 3 sec instead of 6 sec

# Event Loop Flow
# Event Loop
#     │
#     ├── Task 1
#     │      │
#     │      └── await
#     │
#     ├── Task 2
#     │      │
#     │      └── await
#     │
#     └── Task 3
# When one task encounters await, the event loop switches to another task instead of waiting.

# Key Interview Questions
# Q1. What is asynchronous programming?
# - A technique where tasks can pause and allow other tasks to run while waiting for I/O operations.

# Q2. Difference between async and await?
# async defines a coroutine.
# await waits for an async operation inside a coroutine.

# Q3. What is a coroutine?
# - An async function that can suspend and resume execution.

# Q4. What is asyncio?
# - Python's library for writing concurrent asynchronous programs.

# Q5. Difference between concurrency and parallelism?
# Concurrency
# - Multiple tasks make progress together.
# - Usually single thread.
#
# Parallelism
# - Multiple tasks run literally at the same moment.
# - Multiple CPU cores/processes.

# Q6. Why use async programming?
# Ideal for:
# API calls
# Database queries
# Web scraping
# File I/O
# Network applications
# because waiting time can be utilized to execute other tasks efficiently.
