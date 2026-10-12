# 24. Iterators in Python
# 1. Iterable vs Iterator
# Iterable
# - An object that can be looped over using a for loop is called an iterable.
# Examples:
# list
# tuple
# string
# set
# dictionary
numbers = [10, 20, 30]
for num in numbers:
    print(num) # 10 20 30
# numbers is an iterable.

# Iterator
# - An iterator is an object that keeps track of its current position and returns one item at a time.
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it)) # 10
print(next(it)) # 20
print(next(it)) # 30

# Difference
# Iterable -> Iterator
# Can be looped over -> Produces values one by one
# Uses iter() to create iterator -> Uses next() to get next item
# Example: list, tuple, string -> Example: object returned by iter()

nums = [1, 2, 3]      # Iterable
itr = iter(nums)      # Iterator

# 2. iter()
# - The iter() function converts an iterable into an iterator.
# Syntax - iterator = iter(iterable)
fruits = ["Apple", "Banana", "Mango"]
it = iter(fruits)
print(it) # <list_iterator object at 0x0000027D6344CFD0>

# 3. next()
# - The next() function retrieves the next value from an iterator.
fruits = ["Apple", "Banana", "Mango"]
it = iter(fruits)
print(next(it)) # Apple
print(next(it)) # Banana
print(next(it)) # Mango

# When items are exhausted:
print(next(it)) # StopIteration

# Handling StopIteration
nums = [1, 2]
it = iter(nums)
try:
    while True:
        print(next(it))
except StopIteration:
    print("Iterator finished")
# Output:
# 1
# 2
# Iterator finished

# 4. Creating Custom Iterators
# - You can create your own iterator class using:
# __iter__()
# __next__()
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
c = Counter(1, 5)
for num in c:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# 5. __iter__()
# - The __iter__() method returns an iterator object.
# - Python automatically calls it when a loop starts.
class MyIterator:
    def __iter__(self):
        return self
# Example:
nums = [1, 2, 3]
print(nums.__iter__()) # <list_iterator object at ...>

# 6. __next__()
# - The __next__() method returns the next value.
# - When no values remain, it must raise StopIteration.
class Numbers:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > 5:
            raise StopIteration
        value = self.num
        self.num += 1
        return value
n = Numbers()
print(next(n)) # 1
print(next(n)) # 2
print(next(n)) # 3

# Complete Example
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 2
        return value

evens = EvenNumbers(10)

for num in evens:
    print(num)

# Output:
# 2
# 4
# 6
# 8
# 10

# Interview Questions
# Q1. What is the difference between iterable and iterator?
# - Iterable: Object that can be looped over.
# - Iterator: Object that returns values one at a time using next().

# Q2. Why is iter() used?
# - To convert an iterable into an iterator.
it = iter([1, 2, 3])

# Q3. What happens when next() reaches the end?
# - It raises: StopIteration

# Q4. Which methods are required to create a custom iterator?
# __iter__()
# __next__()

# Q5. Can a list be used directly with next()? - NO
nums = [1, 2, 3]
next(nums)      # Error
# Correct:
it = iter(nums)
next(it)
# ✅ Remember: An iterable stores data, while an iterator produces data one item at a time and remembers its current position.

# ------------------------------------------------- #
# 25. Generators (Python)
# A generator is a special type of iterable that produces values one at a time instead of storing all values in memory at once.

# 1. Generator Functions
# - A function containing the yield keyword becomes a generator function.
def numbers():
    yield 1
    yield 2
    yield 3
gen = numbers()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3

# 2. yield
# - The yield statement returns a value and pauses the function's execution. When called again, it continues from where it stopped.
def count():
    yield 1
    yield 2
    yield 3
for num in count():
    print(num) # 1 2 3

# return vs yield
def func1():
    return 10
def func2():
    yield 10
# - return ends the function.
# - yield pauses the function and saves its state.

# 3. Generator Expressions
# - A generator expression is similar to a list comprehension but uses parentheses ().

# List Comprehension
squares = [x * x for x in range(5)]
print(squares) # [0, 1, 4, 9, 16]
# Generator Expression
squares = (x * x for x in range(5))
for num in squares:
    print(num) # 0 1 4 9 16
# - Generators use less memory because values are generated only when needed.

# 4. Lazy Evaluation
# - Generators calculate values only when requested.
def large_numbers():
    for i in range(1000000):
        yield i
gen = large_numbers()
print(next(gen)) # 0
print(next(gen)) # 1
# Here, one million numbers are not created at once. Numbers are generated on demand.

# Benefits
# - Memory efficient
# - Faster for large datasets
# - Suitable for streaming data

# 5. Generator Pipelines
# - Multiple generators can be connected together to process data step by step.
def numbers():
    for i in range(1, 11):
        yield i
def squares(nums):
    for n in nums:
        yield n * n
def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
result = even(squares(numbers()))
for x in result:
    print(x)
# Output
# 4
# 16
# 36
# 64
# 100
# Pipeline Flow: numbers() -> squares() -> even()

# 6. yield from
# - yield from delegates iteration to another iterable or generator.
def gen():
    yield from range(3)
for x in gen():
    print(x)
# Output:
# 0
# 1
# 2

# Another Example
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3

for x in gen2():
    print(x)
# Output
# 1
# 2
# 3

# Interview Questions
# 1. What is a generator?
# - A generator is an iterable that generates values one at a time using yield.

# 2. Why use generators?
# - Generators save memory and are useful when working with large datasets.

# 3. What is the difference between a list and a generator?
# - List
nums = [x for x in range(1000000)]
# Stores all values in memory.
# Faster access by index.

# - Generator
nums = (x for x in range(1000000))
# Generates values on demand.
# Uses much less memory.

# 4. What does yield do?
# - It returns a value and pauses the function while preserving its state.

# 5. What is yield from?
# - It allows one generator to yield values directly from another iterable or generator.

# Practice Questions
# Q1. Generate numbers from 1 to 10
def generate_numbers():
    for i in range(1, 11):
        yield i

# Q2. Generate even numbers from 1 to 20
def even_numbers():
    for i in range(2, 21, 2):
        yield i

# Q3. Create a generator expression for cubes
cubes = (x**3 for x in range(1, 6))
print(list(cubes)) # [1, 8, 27, 64, 125]

# Q4. Combine two lists using yield from
def combine():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
print(list(combine())) # [1, 2, 3, 4, 5, 6]

# Q5. Infinite Generator
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1
# Print the first 5 natural numbers
gen = natural_numbers()
for _ in range(5):
    print(next(gen)) # 1 2 3 4 5

# Key Point for Interviews
# A generator is memory-efficient because it produces values lazily (on demand) rather than storing all values in memory at once.

# ---------------------------------------------- #
# 26. Decorators in Python
# - A decorator is a function (or class) that modifies or extends the behavior of another function or class without changing its original code.

# 1. What is a Decorator?
# Without Decorator
def greet():
    print("Hello!")
greet()

# With Decorator
def decorator_function(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_function
def greet():
    print("Hello!")

greet()

# Output
# Before function call
# Hello!
# After function call

# The line: @decorator_function
# is equivalent to: greet = decorator_function(greet)

# 2. Function Decorators
# A function decorator takes another function as an argument and returns a modified function.

# Logging Decorator
def log_function(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
        print("Function finished")
    return wrapper

@log_function
def say_hi():
    print("Hi")

say_hi()

# Output
# Calling say_hi
# Hi
# Function finished

# 3. Multiple Decorators
# - You can apply more than one decorator to a function.
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def add_exclamation(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@add_exclamation
@uppercase
def message():
    return "hello"

print(message())

# Output: HELLO!!!

# Execution Order
@A
@B
def func():
    pass
# Equivalent to: func = A(B(func))
# B executes first, then A.

# 4. Decorators with Arguments
# - To pass parameters to a decorator, create a decorator factory.
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()

# Output
# Hello
# Hello
# Hello

# Decorator Handling Function Arguments
def logger(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))

# Output
# Arguments: (5, 3) {}
# 8
# *args → positional arguments
# **kwargs → keyword arguments

# 5. functools.wraps
# - A decorator can hide the original function's metadata.
# Problem
def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

@my_decorator
def greet():
    """Greeting function"""
    print("Hello")

print(greet.__name__)

# Output
# wrapper
# The original function name is lost.

# Solution: functools.wraps
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        return func()

    return wrapper

@my_decorator
def greet():
    """Greeting function"""
    print("Hello")

print(greet.__name__)
print(greet.__doc__)

# Output
# greet
# Greeting function

# Benefits:
# Preserves __name__
# Preserves __doc__
# Preserves annotations
# Helps debugging and introspection

# 6. Class Decorators
# - A class can also be used as a decorator by implementing __call__().
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hello")

greet()
greet()
greet()
# Output
# Called 1 times
# Hello
# Called 2 times
# Hello
# Called 3 times
# Hello

# Real-World Uses of Decorators
# Timing Execution
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time:", time.time() - start)
        return result
    return wrapper


from functools import lru_cache

# Authentication
user_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if user_logged_in:
            return func(*args, **kwargs)
        print("Access denied")
    return wrapper


# Logging
def log(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper


# Caching
@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Testing
@login_required
@log
def welcome(name):
    print(f"Welcome, {name}!")


welcome("Aman")

print("Fibonacci:", fibonacci(10))

# Interview Questions
# Q1. What is a decorator?
# - A function (or class) that modifies another function's behavior without changing its source code.


from functools import wraps

# Q2. What does @decorator mean?
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is called")
        return func(*args, **kwargs)
    return wrapper

@decorator
def func():
    pass

# Equivalent to: func = decorator(func)


# Q3. Why use functools.wraps?
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")

print(greet.__name__)  # greet
print(greet.__doc__)   # This function greets the user.


# Q4. Can decorators accept arguments?
# Yes, using a decorator factory.
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def say_hello():
    print("Hello!")

say_hello()  # Prints Hello! five times.


# Q5. What is the order of multiple decorators?
def A(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("A")
        return func(*args, **kwargs)
    return wrapper

def B(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("B")
        return func(*args, **kwargs)
    return wrapper

@A
@B
def func():
    print("Original function")

# Equivalent to: func = A(B(func))
func()

# Summary
# Decorators modify behavior without changing original code.
# @decorator = func = decorator(func).
# Multiple decorators are applied from bottom to top.
# Use *args and **kwargs for flexible decorators.
# functools.wraps preserves metadata.
# Class decorators use __call__().
# Common uses: logging, timing, authentication, caching.

# ----------------------------------------- #