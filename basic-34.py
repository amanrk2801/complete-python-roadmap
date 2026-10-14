# 58. Advanced Python
# These are advanced topics generally asked in senior Python interviews and used in framework development, libraries, and performance optimization.

# 1. Descriptors
# Descriptors allow you to customize attribute access using special methods.
# Methods:
# __get__()
# __set__()
# __delete__()
class Positive:
    def __get__(self, obj, objtype=None):
        return obj._value

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Must be positive")
        obj._value = value


class Product:
    price = Positive()

    def __init__(self, price):
        self.price = price


p = Product(100)
print(p.price)

# Uses
# Properties
# ORM fields (Django, SQLAlchemy)
# Validation systems

# 2. Metaclasses
# - A metaclass creates classes.
# Normal relationship: object → class instance
# Metaclass relationship: type → class
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['version'] = 1.0
        return super().__new__(cls, name, bases, attrs)


class Test(metaclass=MyMeta):
    pass


print(Test.version)

# Output: 1.0

# Uses
# Frameworks
# Enforcing coding rules
# Automatic registration

# 3. __slots__
# Restricts dynamic attribute creation and saves memory.
# Without slots:
class Person:
    pass

p = Person()
p.name = "John"
# With slots:
class Person:
    __slots__ = ['name', 'age']

p = Person()
p.name = "John"

# p.city = "NY"  ❌ Error

# Benefits
# Faster access
# Less memory
# Prevent accidental attributes

# 4. Dynamic Attributes
# Adding attributes at runtime.
class User:
    pass


u = User()

u.name = "Aman"
u.age = 22

print(u.__dict__) # {'name': 'Aman', 'age': 22}

# 5. Monkey Patching
# Modifying code at runtime.
class Dog:
    def sound(self):
        print("Bark")


def new_sound(self):
    print("Woof Woof")


Dog.sound = new_sound

d = Dog()
d.sound()

# Output: Woof Woof
# Uses
# Testing
# Mocking
# Temporary fixes

# 6. Reflection
# Examining or modifying objects dynamically.
class Person:
    def greet(self):
        print("Hello")


p = Person()

method = getattr(p, "greet")
method()

# Output: Hello

# Functions:
# getattr()
# setattr()
# hasattr()
# delattr()

# 7. Introspection
# - Inspecting object information.
x = [1, 2, 3]

print(type(x))
print(dir(x))
print(id(x))
# Output: <class 'list'>
# ...

# Useful functions:
# type()
# id()
# dir()
# isinstance()
# issubclass()

# 8. inspect
# - Provides detailed information about objects.
import inspect

def add(a, b):
    return a + b

print(inspect.signature(add))

# Output: (a, b)
# More examples:
# inspect.getsource(add)
# inspect.isfunction(add)
# inspect.ismethod(add)
# inspect.getmembers(obj)

# 9. functools
# Utilities for higher-order functions.
# lru_cache
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(40))
# partial
from functools import partial

square = partial(pow, exp=2)

print(square(5))
# wraps
from functools import wraps
# Used in decorators.

# 10. itertools
# - Efficient iterator tools.
from itertools import count

for i in count(1):
    if i > 5:
        break
    print(i)
# Common functions:
# cycle()
# repeat()
# chain()
# product()
# permutations()
# combinations()
# groupby()

# Example:
from itertools import combinations

print(list(combinations([1,2,3], 2)))

# Output: [(1,2), (1,3), (2,3)]

# 11. collections
# - Advanced data structures.
# Counter
from collections import Counter

c = Counter("banana")

print(c)

# Output: Counter({'a': 3, 'n': 2, 'b': 1})
# defaultdict
from collections import defaultdict

d = defaultdict(int)

d["a"] += 1

print(d)
# deque
from collections import deque

q = deque([1,2,3])

q.appendleft(0)

print(q)

# 12. operator
# Functional forms of operators.
import operator

print(operator.add(10, 5)) # 15

# Examples:
# operator.sub
# operator.mul
# operator.itemgetter
# operator.attrgetter

# Sorting:
from operator import itemgetter

data = [
    ("Aman", 90),
    ("John", 80)
]

print(sorted(data, key=itemgetter(1)))

# 13. Import Hooks
# - Customize module loading.
import sys

print(sys.meta_path)

# Python searches importers from: sys.meta_path
# Uses:
# Plugin systems
# Custom loaders
# Security checks

# 14. Custom Importers
# - Create your own import mechanism.
import importlib.abc
import importlib.util
# Example skeleton:
class MyImporter(importlib.abc.MetaPathFinder):
    pass
# Used for:
# Loading encrypted modules
# Remote imports
# Plugin architectures

# 15. AST (Abstract Syntax Tree)
# - Python code can be represented as a tree.
import ast

tree = ast.parse("x = 10")

print(ast.dump(tree))

# Output: Module(...)
# Uses
# Linters
# Code analyzers
# Auto code generation

# 16. Bytecode
# Python source code: x = 5 + 2
# ↓
# Compiled to bytecode
# ↓
# Executed by Python VM
# View bytecode:
import dis

def test():
    return 5 + 2

dis.dis(test)

# Output:
# LOAD_CONST
# RETURN_VALUE

# 17. C Extensions
# Write performance-critical code in C.
# Python can call C libraries.
# static PyObject* hello(PyObject* self)
# {
#     printf("Hello");
# }
# Benefits:
# Faster execution
# Access native libraries
# System-level programming

# Examples:
# NumPy
# Pandas
# OpenCV

# 18. Cython
# - C-like syntax for Python performance.
# Python code:
def square(x):
    return x * x
# Cython file:
# cpdef int square(int x):
#     return x * x
# Compile: cythonize -i file.pyx

# Benefits
# Near C speed
# Easy optimization
# Works with Python code

# Quick Revision
# | Topic              | Purpose                    |
# | ------------------ | -------------------------- |
# | Descriptors        | Control attribute access   |
# | Metaclasses        | Create classes             |
# | `__slots__`        | Memory optimization        |
# | Dynamic Attributes | Runtime attributes         |
# | Monkey Patching    | Modify behavior            |
# | Reflection         | Runtime access             |
# | Introspection      | Object inspection          |
# | inspect            | Deep object analysis       |
# | functools          | Function utilities         |
# | itertools          | Iterator utilities         |
# | collections        | Advanced containers        |
# | operator           | Functional operators       |
# | Import Hooks       | Customize imports          |
# | Custom Importers   | User-defined import system |
# | AST                | Code as a tree             |
# | Bytecode           | VM instructions            |
# | C Extensions       | C integration              |
# | Cython             | Faster Python              |

# Interview Questions
# What is the difference between a Descriptor and a Property?
# What are Metaclasses and when should they be used?
# Why does __slots__ reduce memory usage?
# Difference between Reflection and Introspection?
# What is Monkey Patching?
# What is functools.lru_cache?
# Difference between itertools.combinations() and permutations()?
# What is AST used for?
# How can you inspect Python bytecode?
# Difference between C Extensions and Cython?
# Provide your feedback on BizChat
