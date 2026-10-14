# 45. Memory Management in Python
# - Memory management is how Python stores, uses, and frees memory while a program runs.

# 1. Python Memory Model
# - Python manages memory automatically.
# - When you create an object, Python allocates memory for it.
x = 10
name = "Aman"
numbers = [1, 2, 3]
# Memory contains:
# Variables (references)
# Objects
# Internal metadata
x = 100
y = x
# Memory representation:
# x ──► 100
# y ──► 100
# - Both variables point to the same object.

# 2. References
# - Variables do not store actual objects.
# - They store references (addresses) to objects.
a = [1, 2, 3]
b = a
print(a is b)
# Output: True
# - Both variables refer to the same list object.
# a ──┐
#     ├──► [1, 2, 3]
# b ──┘

# 3. Reference Counting
# - Python tracks how many references point to an object.
# - When reference count becomes 0, memory is released.
x = [1, 2, 3]
# Reference count = 1
y = x
# Reference count = 2
del x
# Reference count = 1
del y
# Reference count = 0
# Object is removed from memory.

# Checking Reference Count
import sys

x = []
print(sys.getrefcount(x))
# Output may be: 2
# - Extra reference is created by getrefcount() itself.

# 4. Garbage Collection (GC)
# - Reference counting alone cannot handle circular references.
# Circular Reference
a = []
b = []

a.append(b)
b.append(a)
# a → b
# ↑   ↓
# └───┘
# Even after deleting:
# del a
# del b
# - Objects still reference each other.
# - Python's Garbage Collector removes such unused objects.

# 5. gc Module
# - The gc module controls garbage collection.
# Import: import gc
# Check Status: print(gc.isenabled())
# Output: True
# Disable GC: gc.disable()
# Enable GC: gc.enable()
# Run Garbage Collection: gc.collect()
# Output: 0
# (Number of objects collected)

# View Thresholds: print(gc.get_threshold())
# (700, 10, 10)

# 6. Shallow Copy
# - A shallow copy creates a new outer object but keeps references to nested objects.
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 99

print(original)

# Output: Nested lists are shared.
# Memory View
# original ──► [A, B]
# shallow ──► [A, B]
# A ──► [1,2]
# B ──► [3,4]

# 7. Deep Copy
# - A deep copy creates completely independent objects.
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 99

print(original)
print(deep)
# Output:
# [[1, 2], [3, 4]]
# [[99, 2], [3, 4]]
# - No shared nested objects.

# Memory View
# original ──► [A,B]
# deep ─────► [C,D]
# - Everything is copied.

# 8. copy Module
# - The copy module provides copying operations.
# - import copy
# Shallow Copy
# - copy.copy(obj)
# Deep Copy
# - copy.deepcopy(obj)
import copy

data = [[1,2],[3,4]]

s = copy.copy(data)
d = copy.deepcopy(data)

# 9. Memory Optimization
# - a) Use Generators
# - Lists store all values.
nums = [x*x for x in range(1000000)]
# - Generators create values on demand.
nums = (x*x for x in range(1000000))
# - Uses much less memory.

# b) Use slots
# - Normally:
class Student:
    pass
# Each object has a __dict__.
# Using slots:
class Student:
    __slots__ = ("name", "age")
# Benefits:
# Less memory
# Faster attribute access

# c) Reuse Objects
# - Avoid creating unnecessary objects.
# Bad:
for i in range(100000):
    x = [1, 2, 3]
# Better:
x = [1, 2, 3]

for i in range(100000):
    pass

# d) Delete Unused References
large_data = [0] * 1000000

del large_data
# - Frees memory earlier.

# e) Use Appropriate Data Structures
# - Instead of:
# students = [
#     {"name": "Aman", "age": 23}
# ]
# Use:
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
# - More efficient and cleaner.

# Interview Questions
# Q1. Difference between shallow copy and deep copy?
# Shallow Copy - Deep Copy
# Copies outer object only - Copies all nested objects
# Shared inner objects - Independent objects
# Faster - Slower
# Less memory - More memory

# Q2. Why does Python need Garbage Collection if it uses reference counting?
# - Reference counting cannot clean circular references. Garbage Collection handles them.

# Q3. What is a reference?
# - A variable's connection to an object in memory.
x = [1, 2]
y = x
# - Both variables reference the same object.

# Q4. What does gc.collect() do?
# - It manually triggers garbage collection and removes unreachable objects.

# Q5. What is __slots__?
# - A mechanism that reduces memory usage by preventing the creation of an instance __dict__.
class Employee:
    __slots__ = ("name", "salary")
# - Less memory per object.

# Quick Summary
# Memory Model → Objects live in memory; variables store references.
# References → Multiple variables can point to the same object.
# Reference Counting → Tracks object usage.
# Garbage Collection → Removes circular references.
# gc module → Controls garbage collection.
# Shallow Copy → Copies outer object only.
# Deep Copy → Copies everything recursively.
# copy module → Provides copy() and deepcopy().
# Memory Optimization → Generators, __slots__, deleting unused objects, efficient data structures.

# --------------------------------------------------- #
# 46. Python Internals (Advanced)
# - Python Internals helps you understand how Python works behind the scenes. This knowledge is useful for writing optimized code, debugging complex issues, and understanding advanced frameworks.

# 1. CPython
# - CPython is the most popular implementation of Python.
# When you run: print("Hello")
# CPython performs:
# 1. Parse source code
# 2. Compile to bytecode
# 3. Execute bytecode in Python Virtual Machine (PVM)

# Check Implementation
import platform
print(platform.python_implementation())
# Output: CPython

# Other Implementations
# Implementation - Language
# CPython - C
# PyPy - Python + JIT
# Jython - Java
# IronPython - .NET
# MicroPython - Embedded devices

# 2. Python Bytecode
# - Python doesn't execute source code directly.
# Source Code:
x = 10
y = 20
print(x + y)
# ↓
# Compiled into (Bytecode)
# ↓
# Executed by (Python Virtual Machine (PVM))

# Viewing Bytecode
import dis

def add(a, b):
    return a + b

dis.dis(add)
# Output:
# 2 LOAD_FAST 0 (a)
# 4 LOAD_FAST 1 (b)
# 6 BINARY_ADD
# 8 RETURN_VALUE
# These instructions are bytecode operations.

# Why Bytecode?
# Platform independent
# Faster execution
# Cached in .pyc files

# 3. .pyc Files
# - Python stores compiled bytecode as: module.pyc
# These files:
# Are automatically generated
# Contain bytecode
# Speed up imports
import math
# - Python may compile modules and store bytecode.

# Important
# Deleting .pyc files is safe.
# Python recreates them automatically.

# 4. __pycache__
# - Python stores .pyc files inside:
# project/
# │
# ├── main.py
# └── __pycache__/
#     └── main.cpython-313.pyc

# Why?
# - Different Python versions generate different bytecode.
# main.cpython-311.pyc
# main.cpython-312.pyc
# main.cpython-313.pyc
# - This prevents conflicts.

# Disable Creation
# python -B script.py
# or
# PYTHONDONTWRITEBYTECODE=1

# 5. Interpreter
# - The Python Interpreter is the program that executes Python code.
# Flow:
# Source Code
#     ↓
# Lexer
#     ↓
# Parser
#     ↓
# AST
#     ↓
# Compiler
#     ↓
# Bytecode
#     ↓
# PVM
#     ↓
# Execution

# Interactive Interpreter
# python
# >>> 5 + 10
# 15
# This mode is called:
# REPL
# (REad-Eval-Print Loop)

# 6. GIL (Global Interpreter Lock)
# - One of the most famous CPython concepts.
# What Is It?
# - A lock that allows only one thread at a time to execute Python bytecode.
import threading
# Even if:
# thread1.start()
# thread2.start()
# - Only one thread executes Python bytecode at a moment.

# Why Exists?
# - To make memory management simpler and safer.
# Without GIL: counter += 1
# - could cause data corruption more frequently.

# CPU-Bound Example
import threading

def task():
    for _ in range(10_000_000):
        pass

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
# - Threads won't run truly in parallel on CPU-heavy tasks.

# I/O-Bound Example
# Works well:
# import requests
# import threading
# - While one thread waits for network data, another can run.

# Use Multiprocessing for CPU Work
from multiprocessing import Process
# - Each process has its own Python interpreter and GIL.

# 7. Garbage Collector
# - Python automatically frees unused memory.

# Reference Counting
# - Every object maintains a reference count.
x = [1, 2, 3]
# Reference count: 1
# y = x
# Reference count: 2
# del y
# Reference count: 1
# When it reaches: 0
# Object is destroyed.

# Check Reference Count
import sys
a = []
print(sys.getrefcount(a))

# Cyclic References
# Problem:
a = {}
b = {}

a["b"] = b
b["a"] = a
# Reference counting alone can't clean this.

# Garbage Collector Module
import gc

gc.collect()

# Check statistics:
print(gc.get_count())

# 8. Python Object Model
# Everything in Python is an object.
# x = 10
# Even integers are objects.
# print(type(x))
# Output: <class 'int'>

# Everything Has
# Identity
# Type
# Value
x = 100

print(id(x))
print(type(x))
print(x)

# Classes Are Objects Too
class Test:
    pass

print(type(Test))
# Output: <class 'type'>
# Classes themselves are objects created by the type metaclass.

# 9. Descriptors
# - A descriptor controls attribute access.
# Methods like: @property
# are implemented using descriptors.

# Descriptor Protocol
# A descriptor may define:
__get__()
__set__()
__delete__()

# Example
class Positive:

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        self.value = value


class Product:
    price = Positive()


p = Product()
p.price = 100

print(p.price)

# Output: 100

# Real Uses
# @property
# ORM fields (Django, SQLAlchemy)
# Validation
# Computed attributes

# 10. Metaclasses
# - A metaclass creates classes.
# - Normal object creation: obj = MyClass()
# - Class creation: MyClass = type(...)

# Using type
Person = type(
    "Person",
    (),
    {"name": "Aman"}
)

p = Person()

print(p.name)

# Output: Aman

# Custom Metaclass
class UpperMeta(type):

    def __new__(cls, name, bases, attrs):
        new_attrs = {}

        for k, v in attrs.items():
            if not k.startswith("__"):
                k = k.upper()

            new_attrs[k] = v

        return super().__new__(
            cls,
            name,
            bases,
            new_attrs
        )


class Test(metaclass=UpperMeta):
    value = 100

# Usage: print(Test.VALUE)
# Output: 100

# Uses
# Framework design
# API creation
# ORM systems
# Automatic class registration

# 11. Import System
# - When Python executes: import math
# - It follows these steps:

# Step 1
# Check: sys.modules
# Already loaded? - If yes:
# return existing module

# Step 2
# Search through: sys.path
import sys

print(sys.path)

# Step 3
# - Locate module file:
# math.py
# math.so
# math.pyd
# package/

# Step 4
# Compile if needed
# .py → bytecode

# Step 5
# Execute module

# Step 6
# Store in:
# sys.modules

# Importing a Module Only Once
# module.py
# print("Loaded")
# main.py
# import module
# import module
# Output: Loaded
# - Only once because Python caches modules.

# Interview Questions
# Q1: What is CPython?
# The reference implementation of Python written in C that compiles Python code to bytecode and executes it using the Python Virtual Machine.

# Q2: What is bytecode?
# Intermediate instructions generated from Python source code and executed by the Python Virtual Machine.

# Q3: What is GIL?
# Global Interpreter Lock that allows only one thread at a time to execute Python bytecode in CPython.

# Q4: Difference between .pyc and __pycache__?
# .pyc = compiled bytecode file
# __pycache__ = directory containing .pyc files

# Q5: What is a descriptor?
# An object implementing __get__, __set__, or __delete__ to customize attribute access.

# Q6: What is a metaclass?
# A class that creates other classes. The default metaclass is type.

# Q7: Why are modules imported only once?
# Because imported modules are cached in:
# sys.modules

# Learning Order
# CPython
#    ↓
# Interpreter
#    ↓
# Bytecode
#    ↓
# .pyc
#    ↓
# __pycache__
#    ↓
# Object Model
#    ↓
# Garbage Collector
#    ↓
# GIL
#    ↓
# Descriptors
#    ↓
# Import System
#    ↓
# Metaclasses

# Mastering these topics gives you a deep understanding of how Python works internally and prepares you for advanced frameworks, optimization, and senior-level Python interviews.