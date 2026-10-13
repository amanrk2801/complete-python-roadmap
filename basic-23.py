# 39. Concurrency Concepts
# Concurrency is about handling multiple tasks efficiently. It does not always mean running tasks at the exact same time.

# 1. Concurrency
# Definition: Concurrency means managing multiple tasks that make progress during overlapping time periods.
# Example
# A chef:
# Boils water
# Chops vegetables
# Stirs soup
# The chef switches between tasks instead of finishing one completely before starting another.
# # Conceptual example
# Task A -> work a bit
# Task B -> work a bit
# Task C -> work a bit
# ✅ Multiple tasks are in progress.

# 2. Parallelism
# Definition: Parallelism means multiple tasks execute at the same time.
# Example: Three chefs cooking simultaneously.
# CPU Core 1 → Task A
# CPU Core 2 → Task B
# CPU Core 3 → Task C
# ✅ True simultaneous execution.

# Concurrency vs Parallelism
# Concurrency
# ------------
# Task A ▓▓    ▓▓    ▓▓
# Task B   ▓▓    ▓▓
# Task C      ▓▓    ▓▓
#
# Parallelism
# ------------
# Core1: Task A
# Core2: Task B
# Core3: Task C

# Concurrency = dealing with many tasks.
# Parallelism = doing many tasks simultaneously.

# 3. Threading
# A thread is a lightweight execution unit within a process.
# Uses
# Best for:
# File operations
# API calls
# Web scraping
# Database queries
import threading

def hello():
    print("Hello")

t = threading.Thread(target=hello)
t.start()
t.join()
# Advantages
# ✅ Lightweight
# ✅ Shared memory
# ✅ Good for I/O tasks
# Disadvantages
# ❌ Affected by GIL in CPython
# ❌ Race conditions possible

# 4. Multiprocessing
# - Creates multiple independent processes.
# Each process has:
# - Own memory
# - Own Python interpreter
# - Own GIL
from multiprocessing import Process

def show():
    print("Running")

p = Process(target=show)

p.start()
p.join()

# Advantages
# ✅ Uses multiple CPU cores
# ✅ Good for heavy computation
# ✅ No shared GIL problem
# Disadvantages
# ❌ More memory usage
# ❌ Process creation is expensive

# 5. AsyncIO
# - AsyncIO allows asynchronous programming using:
# async
# await
# Instead of creating threads, a single thread runs many tasks cooperatively.
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(2)
    print("End")

asyncio.run(main())
# Advantages
# ✅ Very efficient
# ✅ Thousands of connections
# ✅ Low memory usage
# Common Uses
# Chat applications
# APIs
# Web servers
# Network programming

# 6. GIL (Global Interpreter Lock)
# The GIL is a lock in CPython that allows only one thread to execute Python bytecode at a time.
# Effect
# Thread 1 → running Python code
# Thread 2 → waiting
#
# Thread 1 releases GIL
# Thread 2 runs

#Because of GIL
# CPU-heavy
for i in range(100000000):
    pass
# Multiple threads usually do not speed up CPU-bound work.

# GIL does NOT hurt much for
# Network requests
# File operations
# Database calls
# - because threads spend most time waiting.

# 7. CPU-bound Tasks
# - Tasks that spend most of their time using the CPU.
# Examples
# Prime number calculation
# Image processing
# Machine learning training
# Video encoding
# Scientific computations
for i in range(10**8):
    pass
# Best Choice
# ✅ Multiprocessing
# CPU-bound → Multiprocessing

# 8. I/O-bound Tasks
# - Tasks waiting for external resources.
# Examples
# Reading files
# Database queries
# API requests
# Web scraping
# Downloading files
# response = requests.get(url)
# Most of the time is spent waiting for data.
# Best Choice: ✅ Threading
# or
# ✅ AsyncIO
# I/O-bound → Threading / AsyncIO

# Quick Comparison
# Feature - Threading - Multiprocessing
# Unit - Thread - Process
# Memory - Shared - Separate
# CPU-bound - Poor - Excellent
# I/O-bound - Good - Good
# Multiple CPU Cores - No (GIL) - Yes
# Complexity - Easy - Medium

# Interview Questions
# Q1: Difference between concurrency and parallelism?
# - Concurrency: Multiple tasks make progress together.
# - Parallelism: Multiple tasks execute at the same instant.

# Q2: What is GIL?
# Global Interpreter Lock that allows only one thread to execute Python bytecode at a time.

# Q3: When should multiprocessing be used?
# For CPU-intensive tasks such as calculations, image processing, and machine learning.

# Q4: When should AsyncIO be used?
# - For high-volume I/O operations such as APIs, web servers, and network applications.

# Memory Trick
# CPU-bound  → Multiprocessing
# I/O-bound  → Threading or AsyncIO
#
# Threading      = Many workers, one CPU lane
# Multiprocessing = Many workers, many CPU lanes
# AsyncIO        = One worker managing many waiting tasks

# ---------------------------------------- #
# 40. Testing in Python
# - Testing is the process of verifying that your code works as expected and continues to work after changes.
# 1. unittest
# - unittest is Python's built-in testing framework inspired by Java's JUnit.
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

# Test Cases
# - A test case is a class that contains test methods.
import unittest

class TestString(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isdigit(self):
        self.assertTrue("123".isdigit())

# Assertions
# - Assertions check whether a condition is true.
# Common Assertions
# self.assertEqual(a, b)
# self.assertNotEqual(a, b)
#
# self.assertTrue(condition)
# self.assertFalse(condition)
#
# self.assertIs(a, b)
# self.assertIsNone(value)
#
# self.assertIn(item, collection)
#
# self.assertRaises(Exception)

def divide(a, b):
    return a / b

class TestDivide(unittest.TestCase):

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

# Test Suites
# - A Test Suite groups multiple test cases.
import unittest

class TestA(unittest.TestCase):
    def test_a(self):
        pass

class TestB(unittest.TestCase):
    def test_b(self):
        pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestA))
suite.addTest(unittest.makeSuite(TestB))

runner = unittest.TextTestRunner()
runner.run(suite)

# Setup and Teardown
# - Used to prepare and clean up before/after tests.
import unittest

class TestExample(unittest.TestCase):

    def setUp(self):
        print("Before each test")

    def tearDown(self):
        print("After each test")

    def test_one(self):
        print("Test 1")

    def test_two(self):
        print("Test 2")

# Execution Order:
# setUp()
# test_one()
# tearDown()
#
# setUp()
# test_two()
# tearDown()

# 2. pytest
# - pytest is a popular third-party testing framework that is simpler and more powerful than unittest.
# Install: pip install pytest
# Run: pytest

# Basic Example
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
# Run: pytest test_file.py

# Fixtures: Fixtures provide reusable setup code.
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_length(sample_data):
    assert len(sample_data) == 3

# Parametrization
# - Run the same test with multiple inputs.
import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (1, 2, 3),
        (2, 3, 5),
        (5, 5, 10)
    ]
)
def test_add(a, b, result):
    assert a + b == result

# Markers: Used to categorize tests.
import pytest

@pytest.mark.slow
def test_large_file():
    pass

@pytest.mark.database
def test_db():
    pass
# Run a specific marker: pytest -m database

# Mocking
# - Mocking replaces real objects/functions during testing.
from unittest.mock import Mock

api = Mock()
api.get_user.return_value = {"name": "John"}

result = api.get_user()

print(result)

# Output: {'name': 'John'}

# Example:
from unittest.mock import patch

@patch("module.function")
def test_function(mock_func):
    mock_func.return_value = 100

    result = mock_func()

    assert result == 100

# Coverage
# - Measures how much code is tested.
# Install: pip install pytest-cov
# Run: pytest --cov=myproject
# HTML Report: pytest --cov=myproject --cov-report=html

# 3. Unit Testing
# - Tests individual functions or methods in isolation.
def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
# ✅ Fast
# ✅ Easy to debug
# ✅ No external dependencies

# 4. Integration Testing
# - Tests interaction between multiple components.
def save_user(db, name):
    db.append(name)

def get_users(db):
    return db

def test_integration():
    db = []

    save_user(db, "Aman")

    assert get_users(db) == ["Aman"]
# Checks communication between components.

# 5. End-to-End (E2E) Testing
# Tests the complete application flow from user perspective.
# User Login
#     ↓
# Dashboard Opens
#     ↓
# Create Order
#     ↓
# Order Saved
#     ↓
# Logout

# Tools:
# Selenium
# Playwright
# Cypress

# Example (Playwright):
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("https://example.com")

    assert "Example" in page.title()

    browser.close()

# 6. Test-Driven Development (TDD)
# - TDD means writing tests before writing the actual code.
# Process
# 1. Write a failing test
#        ↓
# 2. Run test (FAIL)
#        ↓
# 3. Write minimal code
#        ↓
# 4. Run test (PASS)
#        ↓
# 5. Refactor
#        ↓
# 6. Repeat

# Step 1: Write Test
def test_add():
    assert add(2, 3) == 5
# Test fails because add() doesn't exist.

# Step 2: Write Code
def add(a, b):
    return a + b

# Step 3: Run Test
# PASSED

# unittest vs pytest
# Feature - unittest - pytest
# Built into Python - ✅ - ❌
# Easy syntax - ❌ - ✅
# Assertions - Verbose - Simple
# Fixtures - Limited - Powerful
# Parametrization - No - Yes
# Plugins - Few - Many
# Popularity - High - Very High

# Interview Questions
# What is testing?
# Testing is the process of verifying that software behaves as expected.

# Difference between unittest and pytest?
# unittest is built into Python and uses classes, while pytest provides simpler syntax, fixtures, parametrization, and powerful plugins.

# What is a fixture?
# A reusable setup function used before tests run.

# What is mocking?
# Replacing real objects or functions with fake ones during testing.

# What is TDD?
# A development methodology where tests are written before implementation code.

# Difference between Unit, Integration, and E2E Testing?
# Unit Testing → Tests a single function/class.
# Integration Testing → Tests interaction between components.
# End-to-End Testing → Tests the entire application flow.