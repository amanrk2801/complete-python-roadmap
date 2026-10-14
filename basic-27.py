# 47. Performance & Optimization in Python
# Performance optimization means making your code run faster, use less memory, and handle larger datasets efficiently.

# 1. Big-O Basics
# - Big-O notation describes how an algorithm's performance changes as input size grows.
# Common Complexities
# Complexity - Name - Example
# O(1) - Constant - List indexing
# O(log n) - Logarithmic - Binary search
# O(n) - Linear - Loop through list
# O(n log n) - Linearithmic - Efficient sorting
# O(n²) - Quadratic - Nested loops
# O(2ⁿ) - Exponential - Recursive Fibonacci

# Example
# O(n)
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# O(n²)
for i in nums:
    for j in nums:
        print(i, j)

# Why It Matters
# For 10 items:
# O(n) → 10 operations
# O(n²) → 100 operations

# For 1,000,000 items:
# O(n) → 1,000,000
# O(n²) → 1,000,000,000,000
# Huge difference!

# 2. Profiling
# - Profiling helps identify slow parts of a program.
# Instead of guessing: ❌ "I think this loop is slow"
# Use profiling: ✅ "This function consumes 80% of execution time"

# 3. timeit
# - Used to measure execution time accurately.
import timeit

result = timeit.timeit(
    stmt="[x*x for x in range(1000)]",
    number=1000
)

print(result) # 0.0845

# Comparing Two Methods
import timeit

list_time = timeit.timeit(
    stmt="[i for i in range(1000)]",
    number=10000
)

loop_time = timeit.timeit(
    stmt="""
lst = []
for i in range(1000):
    lst.append(i)
""",
    number=10000
)

print("List comprehension:", list_time)
print("For loop:", loop_time)

# Usually:
# List comprehension: Faster
# For loop: Slower

# 4. cProfile
# - Used to profile an entire program.
import cProfile

def square_sum():
    total = 0

    for i in range(100000):
        total += i*i

    return total

cProfile.run("square_sum()")
# Output: 4 function calls in 0.012 seconds

# Save Profile Output
import cProfile

cProfile.run("square_sum()", "profile.stats")

# 5. time Module
# - Simple timing measurements.
import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print(end - start) # 0.03

# Better Precision
import time

start = time.perf_counter()

for i in range(1000000):
    pass

end = time.perf_counter()

print(end - start)
# perf_counter() is preferred for benchmarking.

# 6. Memory Profiling
# Measures memory usage.
# Using sys.getsizeof
import sys

nums = [1, 2, 3]

print(sys.getsizeof(nums)) # 88

# Using memory_profiler
# Install: pip install memory-profiler
from memory_profiler import profile

@profile
def create_list():
    return [i for i in range(100000)]

create_list()

# Run: python -m memory_profiler file.py

# 7. Algorithm Optimization
# - Fast algorithms matter more than fast hardware.
# Slow
def contains(lst, target):
    for item in lst:
        if item == target:
            return True
# Complexity: O(n)

# Better Using Set
data = set(range(100000))

print(99999 in data)
# Complexity: O(1)

# 8. Data Structure Selection
# - Choosing the right structure dramatically improves performance.

# List
# nums = [1, 2, 3]
# Good for:
# Ordered data
# Index access
# nums[2]
# O(1)

# Set
# nums = {1, 2, 3}
# Good for:
# Membership testing
# 3 in nums
# O(1)

# Dictionary
student = {
    "name": "Aman",
    "age": 22
}
# Lookup:
# student["name"]
# O(1)

# Deque
from collections import deque
dq = deque()
# Fast insert/remove from both ends.
dq.appendleft(10)
# O(1)

# 9. Lazy Evaluation
# - Values are created only when needed.
# Generator
def numbers():
    for i in range(1000000):
        yield i
# No giant list is stored.

# List
nums = [i for i in range(1000000)]
# Creates all elements immediately.

# Generator
nums = (i for i in range(1000000))
# Creates values one at a time.
# Memory efficient.

# 10. Caching
# - Caching stores previously computed results.
# Without cache:
def square(n):
    print("Calculating...")
    return n*n

square(10)
square(10)
# Output
# Calculating...
# Calculating...
# Calculation repeated.

# Manual Cache
cache = {}

def square(n):
    if n in cache:
        return cache[n]

    result = n*n
    cache[n] = result
    return result

# 11. functools.lru_cache
# Least Recently Used cache.
# Automatically caches function results.
from functools import lru_cache

@lru_cache(maxsize=128)
def square(n):
    print("Calculating...")
    return n*n

print(square(10))
print(square(10))
# Output:
# Calculating...
# 100
# 100
# Second call is retrieved from cache.

# Fibonacci Optimization
# Without Cache
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
# Complexity: O(2^n)
# Very Slow

# With lru_cache
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

print(fib(50))
# Complexity becomes approximately: O(n)
# Huge improvement.

# Performance Optimization Best Practices
# ✅ Choose efficient algorithms first
# ✅ Use appropriate data structures
# ✅ Profile before optimizing
# ✅ Use generators for large data
# ✅ Cache expensive computations
# ✅ Use timeit for benchmarks
# ✅ Use cProfile for full-program profiling
# ✅ Prefer sets/dictionaries for lookups
# ✅ Avoid unnecessary loops
# ✅ Measure performance after every optimization

# Interview Questions
# Q1. What is Big-O notation?
# It describes how execution time or memory grows with input size.

# Q2. Difference between timeit and time?
# timeit → Accurate benchmarking
# time → General timing

# Q3. What does cProfile do?
# - Profiles function calls and execution time.

# Q4. Why are sets faster than lists for lookup?
# Sets use hash tables, giving approximately O(1) lookup time.

# Q5. What is lazy evaluation?
# Values are generated only when needed instead of all at once.

# Q6. What is lru_cache?
# A decorator that automatically caches function results to avoid recalculation.

# ---------------------------------------------- #
# 48. Security (Python)
# Security is the practice of protecting applications, data, and systems from unauthorized access, attacks, and misuse.
# 1. Input Validation
# Input validation ensures that user-provided data is safe and in the expected format before processing.
# Why Important?
# Prevents malicious input.
# Reduces application crashes.
# Helps prevent SQL Injection, Command Injection, etc.

# Bad Example: age = int(input("Enter age: "))
# If user enters: abc (Program crashes.)

# Good Example
age = input("Enter age: ")

if age.isdigit():
    age = int(age)
    print(age)
else:
    print("Invalid input")

# Email Validation
import re

email = "user@example.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# 2. Secure Password Handling
# - Never store passwords in plain text.
# Wrong
# password = "mypassword123"
# Database stores:
# mypassword123
# Anyone can read it.
# Correct (Hashing)
import hashlib

password = "mypassword123"

hashed = hashlib.sha256(password.encode()).hexdigest()

print(hashed)

# Better: bcrypt
import bcrypt

password = b"mypassword123"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

# Verify: bcrypt.checkpw(password, hashed)

# Best Practices
# ✅ Use bcrypt, argon2, or scrypt
# ✅ Never store plain passwords
# ✅ Use salt
# ✅ Enforce strong passwords

# 3. Environment Variables
# Sensitive information should not be hardcoded.
# Wrong: DB_PASSWORD = "admin123"
# Correct
import os
DB_PASSWORD = os.getenv("DB_PASSWORD")
# Set variable:
# Linux/Mac: export DB_PASSWORD=mysecret
# Windows: set DB_PASSWORD=mysecret
import os

api_key = os.getenv("API_KEY")

print(api_key)

# 4. Secrets Management
# Secrets include:
# Database passwords
# API Keys
# Tokens
# Certificates
# Don't Store: API_KEY = "secret123"

# Use
# Azure Key Vault
# AWS Secrets Manager
# HashiCorp Vault
# Kubernetes Secrets
# Example (.env)
# API_KEY=abc123
# DB_PASSWORD=admin

# Python:
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

# 5. SQL Injection
# SQL Injection occurs when attackers manipulate SQL queries through user input.
# Dangerous
username = input("Username: ")
query = f"SELECT * FROM users WHERE username='{username}'"

# Input: ' OR '1'='1
# Query becomes: SELECT * FROM users WHERE username='' OR '1'='1'
# Can expose all records.
# Safe Method
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")

cursor.execute(
    "SELECT * FROM users WHERE username=?",
    (username,)
)
# Rule
# ✅ Use parameterized queries
# ✅ Use ORM (SQLAlchemy, Django ORM)
# ❌ Never concatenate SQL strings

# 6. Command Injection
# Occurs when user input is executed as a system command.
# Dangerous
import os

filename = input("File: ")

os.system(f"cat {filename}")
# Input: file.txt; rm -rf /
# Safe
import subprocess

filename = "file.txt"

subprocess.run(
    ["cat", filename],
    check=True
)
# Rules
# ✅ Avoid os.system()
# ✅ Avoid shell=True
# ✅ Validate user input

# 7. Path Traversal
# Attackers access files outside intended directories.
# Dangerous
file = input("Filename: ")

with open(file) as f:
    print(f.read())
# Input: ../../etc/passwd

# Safe
from pathlib import Path

BASE_DIR = Path("uploads")

filename = input("File: ")

path = (BASE_DIR / filename).resolve()

if BASE_DIR.resolve() in path.parents:
    print(path.read_text())
else:
    print("Access denied")

# Protect Against
# ../
# ../../
# ..\\

# 8. Authentication
# Authentication = Verifying identity.
# Question: Who are you?
# Examples:
# Username + Password
# OTP
# Fingerprint
# OAuth Login

# Simple Example
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secret":
    print("Login Successful")

# Real applications use:
# - Password Hashing
# - JWT Tokens
# - Session Cookies
# - MFA (Multi-Factor Authentication)

# 9. Authorization
# Authorization = Determining permissions.
# Question: What are you allowed to do?
# Example
# User logged in successfully:
role = "user"

if role == "admin":
    print("Can delete records")
else:
    print("Access denied")
# Difference
# Authentication → Identity verification
# Authorization  → Permission verification

# Example:
# Login to bank account          -> Authentication
# Transfer money                -> Authorization

# 10. Dependency Vulnerabilities
# Modern applications use third-party packages.
# Some packages may contain security flaws.

# Check Installed Packages: pip list
# Find Vulnerabilities:
# pip install pip-audit
# pip-audit
#  Check Outdated Packages: pip list --outdated
# Update Package: pip install --upgrade requests
# requirements.txt
# requests==2.32.0
# flask==3.0.3

# Best Practices
# ✅ Keep dependencies up to date
# ✅ Remove unused libraries
# ✅ Use trusted packages
# ✅ Regularly scan for vulnerabilities

# Security Checklist
# ✅ Validate all user inputs
# ✅ Hash passwords using bcrypt/argon2
# ✅ Use environment variables
# ✅ Store secrets securely
# ✅ Use parameterized SQL queries
# ✅ Avoid shell=True and os.system()
# ✅ Prevent path traversal
# ✅ Implement authentication
# ✅ Implement authorization
# ✅ Keep dependencies updated
# ✅ Use HTTPS
# ✅ Enable logging and monitoring
# ✅ Follow least privilege principle

# Interview Questions
# Q1. What is SQL Injection?
# An attack where malicious SQL code is inserted into user input to manipulate database queries.

# Q2. Difference between Authentication and Authorization?
# Authentication -> Who are you?
# Authorization  -> What can you do?

# Q3. Why shouldn't passwords be stored in plain text?
# If the database is compromised, attackers can immediately see all passwords.

# Q4. What are environment variables?
# Variables stored outside the code that hold configuration and sensitive information.

# Q5. Why is bcrypt preferred over SHA-256 for passwords?
# bcrypt is designed for password hashing, includes salting, and is intentionally slow, making brute-force attacks much harder.

# Q6. What is Path Traversal?
# An attack where users access files outside the intended directory using paths like:
# ../../etc/passwd

# Q7. What is Command Injection?
# An attack where malicious user input is executed as an operating system command.

# Q8. What is Secrets Management?
# Secure storage and retrieval of sensitive information such as API keys, tokens, and passwords.

# Q9. What is the Principle of Least Privilege?
# Users and applications should be given only the minimum permissions required to perform their tasks.

# Q10. How can you check Python dependency vulnerabilities?
# pip-audit
# 0r
# safety check