# 59. Python Standard Library - Important Modules
# The Python Standard Library is a collection of built-in modules that come with Python, so you don't need to install them separately.

# 1. os
# Used for interacting with the operating system.
import os

print(os.getcwd())      # Current directory
os.mkdir("test")        # Create folder
print(os.listdir())     # List files/folders

# Common functions:
# os.getcwd()
# os.chdir()
# os.mkdir()
# os.remove()
# os.listdir()
# os.environ

# 2. sys
# Provides access to Python interpreter information.
import sys

print(sys.version)
print(sys.platform)
print(sys.argv)

# Common:
# sys.argv
# sys.path
# sys.exit()
# sys.version

# 3. math
# Mathematical functions.
import math

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))

# Common:
# sqrt()
# ceil()
# floor()
# pow()
# factorial()
# sin(), cos()

# 4. random
# Generate random values.
import random

print(random.randint(1, 10))
print(random.choice(["A", "B", "C"]))

# Common:
# randint()
# random()
# choice()
# shuffle()
# sample()

# 5. datetime
# Date and time handling.
from datetime import datetime

now = datetime.now()
print(now)

# Common:
# date
# time
# datetime
# timedelta

# 6. time
# Time-related operations.
import time

print(time.time())
time.sleep(2)
print("Done")

# Common:
# sleep()
# time()
# ctime()

# 7. json
# Work with JSON data.
import json

data = {"name": "Aman"}

json_str = json.dumps(data)
print(json_str)

# Common:
# loads()
# dumps()
# load()
# dump()

# 8. csv
# Read and write CSV files.
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Common:
# reader()
# writer()
# DictReader()
# DictWriter()

# 9. re
# Regular Expressions.
import re

text = "Python123"

result = re.findall(r"\d+", text)
print(result)

# Common:
# match()
# search()
# findall()
# sub()
# split()

# 10. collections
# Special container datatypes.
from collections import Counter

data = ["a", "b", "a"]
print(Counter(data))

# Important:
# Counter
# defaultdict
# deque
# namedtuple

# 11. itertools
# Efficient looping tools.
from itertools import permutations

print(list(permutations([1, 2, 3])))
# Important:
# product()
# permutations()
# combinations()
# cycle()
# count()

# 12. functools
# Functional programming helpers.
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, nums)
print(result)

# Common:
# reduce()
# lru_cache()
# partial()
# wraps()

# 13. operator
# Functions corresponding to operators.
import operator

print(operator.add(10, 20))
# Common:
# add()
# sub()
# mul()
# itemgetter()
# attrgetter()

# 14. pathlib
# Modern path handling.
from pathlib import Path

path = Path("file.txt")

print(path.exists())

# Common:
# Path()
# exists()
# mkdir()
# rename()

# 15. shutil
# High-level file operations.
import shutil

shutil.copy("a.txt", "b.txt")

# Common:
# copy()
# copytree()
# move()
# rmtree()

# 16. subprocess
# Run external programs.
import subprocess

subprocess.run(["dir"], shell=True)
# Common:
# run()
# Popen()
# check_output()

# 17. logging
# Application logging.
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")

# Levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# 18. argparse
# Command-line arguments.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")

args = parser.parse_args()

print(args.name)

# 19. statistics
# Statistical calculations.
import statistics

data = [10, 20, 30]

print(statistics.mean(data))

# Common:
# mean()
# median()
# mode()
# stdev()

# 20. decimal
# Precise decimal arithmetic.
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))

# Output: 0.3

# 21. fractions
# Fraction arithmetic.
from fractions import Fraction

f = Fraction(3, 4)

print(f)

# 22. sqlite3
# SQLite database.
import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER)"
)

conn.commit()
conn.close()

# 23. threading
# Multithreading.
import threading

def show():
    print("Thread running")

t = threading.Thread(target=show)

t.start()
t.join()

# 24. multiprocessing
# Multiple processes.
from multiprocessing import Process

def show():
    print("Process running")

p = Process(target=show)

p.start()
p.join()

# 25. asyncio
# Asynchronous programming.
import asyncio

async def main():
    print("Hello")

asyncio.run(main())

# Keywords:
# async
# await
# Task
# Event Loop

# 26. typing
# Type hints.
from typing import List

nums: List[int] = [1, 2, 3]

# Common:
# List
# Dict
# Tuple
# Optional
# Union

# 27. dataclasses
# Automatic class generation.
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

s = Student("Aman", 21)

print(s)

# 28. enum
# Enumerations.
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2

print(Color.RED)

# 29. abc
# Abstract Base Classes.
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# 30. copy
# Object copying.
import copy

a = [1, 2, [3, 4]]

b = copy.deepcopy(a)

print(b)

# Types:
# copy()
# deepcopy()

# 31. pickle
# Object serialization.
import pickle

data = {"name": "Aman"}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    obj = pickle.load(f)

print(obj)

# Most Important Modules for Interviews
# Focus first on:
# os
# sys
# math
# datetime
# json
# csv
# re
# collections
# itertools
# functools
# pathlib
# subprocess
# logging
# sqlite3
# threading
# asyncio
# typing
# dataclasses
# These are the modules that appear most frequently in real-world Python development and interviews.
