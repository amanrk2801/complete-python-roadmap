# 41. Logging in Python
# Logging is used to record messages about a program's execution. It helps in debugging, monitoring, and troubleshooting applications.
# 1. logging Module
# - Python provides a built-in logging module.
import logging
logging.warning("This is a warning message")
# Output: WARNING:root:This is a warning message

# 2. Log Levels
# - Logging levels indicate the severity of events.
# Level - Value - Purpose
# DEBUG - 10 - Detailed information for debugging
# INFO - 20 - General information
# WARNING - 30 - Something unexpected happened
# ERROR - 40 - A serious problem occurred
# CRITICAL - 50 - Program may stop running

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
# Output
# DEBUG:root:Debug message
# INFO:root:Info message
# WARNING:root:Warning message
# ERROR:root:Error message
# CRITICAL:root:Critical message

# 3. Logger
# - A logger is the object that creates log messages.
import logging
logger = logging.getLogger("my_logger")
logger.warning("Something happened")

# 4. Handler
# - Handlers decide where logs are sent.
# Examples
# Console
# File
# Email
# Network
import logging
logger = logging.getLogger("app")
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.warning("Displayed on console")

# 5. Formatter
# - Formatters control how log messages appear.
import logging
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger("app")
logger.addHandler(handler)
logger.warning("Test message")

# Output: 2026-10-14 10:00:00,123 - WARNING - Test message
# Common format fields:
# %(asctime)s
# %(name)s
# %(levelname)s
# %(message)s
# %(filename)s
# %(lineno)d

# 6. File Logging
# - Save logs to a file.
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application started")
logging.error("An error occurred")
# - Contents of app.log:
# INFO:root:Application started
# ERROR:root:An error occurred

# 7. Rotating Logs
# - Large log files can consume disk space.
# - Use RotatingFileHandler:
from logging.handlers import RotatingFileHandler
import logging

handler = RotatingFileHandler(
    "app.log",
    maxBytes=1000,
    backupCount=3
)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

for i in range(100):
    logger.info(f"Log message {i}")
# Example generated files:
# app.log
# app.log.1
# app.log.2
# app.log.3

# 8. Structured Logging
# - Logs are stored in a structured format such as JSON.
import json
import logging

data = {
    "user": "Aman",
    "action": "login",
    "status": "success"
}

logging.info(json.dumps(data))
# Output:
# {"user": "Aman", "action": "login", "status": "success"}
# This format is useful for:
# ELK Stack (Elasticsearch, Logstash, Kibana)
# Splunk
# CloudWatch
# Datadog

# Complete Example
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler(
    "app.log",
    maxBytes=100000,
    backupCount=5
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Low disk space")
logger.error("Database connection failed")
logger.critical("System crash")

# Interview Questions
# 1. Difference between print() and logging?
# print() displays output only on console.
# logging supports levels, files, formatting, filtering, and handlers.

# 2. What is a Logger?
# An object responsible for generating log messages.

# 3. What is a Handler?
# A component that sends logs to a destination such as console or file.

# 4. What is a Formatter?
# It defines the log message format.

# 5. Why use RotatingFileHandler?
# To prevent log files from growing indefinitely.

# 6. Which log level is used for debugging?
# DEBUG

# 7. Which level is highest?
# CRITICAL

# Log Level Order (Low → High)
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Remember:
#  Logger → creates logs
#  Handler → sends logs
#  Formatter → formats logs
#  Level → defines severity of logs

# ----------------------- #
# 42. Debugging in Python
# - Debugging is the process of finding and fixing errors (bugs) in a program.
# 1. Debugger
# - A debugger is a tool that allows you to execute a program step-by-step, inspect variables, and find bugs.
# Benefits
# Pause execution
# Check variable values
# Execute code line by line
# Understand program flow

# Example Bug
a = 10
b = 0
result = a / b
print(result)
# Output: ZeroDivisionError: division by zero
# - A debugger helps identify exactly where the error occurred.

# 2. Breakpoints
# - A breakpoint is a marker where program execution stops temporarily.
x = 10
y = 20
z = x + y   # Breakpoint here
print(z)
# When execution reaches the breakpoint:
# Program pauses
# Variables can be inspected
# Code can be executed line-by-line
# Uses
# ✅ Check values before an error occurs
# ✅ Verify program logic
# ✅ Inspect variable states

# 3. Stack Traces
# - When an error occurs, Python displays a stack trace.
# It shows:
# Which files were executed
# Which functions were called
# The exact line causing the error
def divide(a, b):
    return a / b
divide(10, 0)
# Output:
# Traceback (most recent call last):
#   File "test.py", line 4, in <module>
#     divide(10, 0)
#
#   File "test.py", line 2, in divide
#     return a / b
#
# ZeroDivisionError: division by zero

# Reading Stack Trace
# Read from bottom to top:
# ZeroDivisionError: division by zero
# Actual error.
# return a / b
# Error location.
# divide(10, 0)
# Function call that triggered the error.

# 4. pdb (Python Debugger)
# - pdb is Python's built-in debugger.
# Starting pdb
import pdb
pdb.set_trace()
x = 10
y = 20
z = x + y
print(z)
# Execution stops at: (Pdb)

# Common pdb Commands
# Command - Meaning
# n - Next line
# s - Step into function
# c - Continue execution
# l - List source code
# p var - Print variable
# q - Quit debugger

# (Pdb) p x
# 10
#
# (Pdb) p y
# 20
#
# (Pdb) n
#
# (Pdb) p z
# 30

# Running Script with pdb
# - python -m pdb app.py

# 5. IDE Debugging
# - Modern IDEs provide graphical debugging tools.
# VS Code
# Features:
# Breakpoints
# Variable Inspector
# Watch Window
# Call Stack
# Step Over
# Step Into
# Continue

# Debug Buttons
# Button - Action
# ▶ - Continue
# ⬇ - Step Into
# ⤴ - Step Out
# ↷ - Restart
# ⏹ - Stop

# PyCharm
# Features:
# Smart breakpoints
# Variable viewer
# Expression evaluation
# Debug console
# Example:
# Click line number
# Red dot appears
# Press Debug
# Execution pauses at breakpoint

# 6. Reading Exceptions
# - An exception is a runtime error.
numbers = [1, 2, 3]
print(numbers[10])
# Output: IndexError: list index out of range

# Common Exceptions
# ZeroDivisionError
# 10 / 0 -> ZeroDivisionError

# ValueError
# int("abc") -> ValueError

# TypeError
# "10" + 5 -> TypeError

# NameError
# print(age) -> NameError

# KeyError
student = {"name": "Aman"}
print(student["age"]) # KeyError

# FileNotFoundError
open("data.txt") # FileNotFoundError

# Exception Reading Strategy
# When an error occurs:
# 1. Read the last line first
# 2. Identify exception type
# 3. Find file and line number
# 4. Check variable values
# 5. Reproduce and fix

# 7. Profiling
# - Profiling is used to measure program performance.
# It answers:
# Which function is slow?
# Which code uses most CPU?
# How much time is spent in each function?

# Using time Module
import time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print(end - start) # 0.03

# Using timeit
import timeit

result = timeit.timeit(
    "sum(range(100))",
    number=10000
)

print(result)

# Using cProfile
import cProfile

def square():
    for i in range(100000):
        i * i

cProfile.run("square()")
# Output:
# ncalls  tottime  percall
# 1       0.012    0.012

# Finding Bottlenecks
# Bad:
result = []

for i in range(100000):
    result.append(i)

# Better:
result = [i for i in range(100000)]
# Profiling helps discover such optimizations.

# Debugging Workflow
# Error Occurs
#       ↓
# Read Exception
#       ↓
# Read Stack Trace
#       ↓
# Add Breakpoint
#       ↓
# Inspect Variables
#       ↓
# Use pdb/IDE Debugger
#       ↓
# Fix Bug
#       ↓
# Profile Performance (if needed)

# Interview Questions
# Q1. What is a breakpoint?
#  A breakpoint pauses program execution so you can inspect variables and program state.

# Q2. What is pdb?
#  pdb is Python's built-in debugger used for step-by-step debugging.

# Q3. How do you start pdb?
# import pdb
# pdb.set_trace()
# or
# python -m pdb script.py

# Q4. What is a stack trace?
# - A stack trace shows the sequence of function calls that led to an exception.

# Q5. What is profiling?
# - Profiling measures performance and identifies slow parts of a program.

# Q6. Which module is commonly used for profiling?
# - cProfile and timeit.