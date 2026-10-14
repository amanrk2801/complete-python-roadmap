# 57. Software Engineering Practices
# Software Engineering Practices help developers write maintainable, scalable, readable, and reliable software. These principles are essential in real-world projects.

# 1. Clean Code
# - Clean code is code that is easy to read, understand, and maintain.
# Characteristics
# - Meaningful variable names
# - Small functions
# - Proper comments
# - Consistent formatting
# - Avoid duplicated logic

# Bad Example
x = 5
y = 10
z = x * y
print(z)

# Good Example
price = 5
quantity = 10
total_cost = price * quantity

print(total_cost)

# Guidelines
# ✅ Use descriptive names
# ✅ Keep functions short
# ✅ One function = one responsibility
# ✅ Remove unused code

# 2. SOLID Principles
# Five object-oriented design principles.
# S - Single Responsibility Principle (SRP)
# - A class should have only one reason to change.
# Bad
class User:
    def save(self):
        pass

    def send_email(self):
        pass
# Good
class User:
    def save(self):
        pass

class EmailService:
    def send_email(self):
        pass

# O - Open/Closed Principle (OCP)
# - Open for extension, closed for modification.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# - New shapes can be added without modifying existing code.

# L - Liskov Substitution Principle (LSP)
# Subclasses should replace parent classes without breaking functionality.
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

# I - Interface Segregation Principle (ISP)
# - Clients should not depend on methods they do not use.
from abc import ABC

class Printer(ABC):
    def print_doc(self):
        pass

# D - Dependency Inversion Principle (DIP)
# - Depend on abstractions, not concrete implementations.
class Database:
    def save(self):
        pass

class UserService:
    def __init__(self, db):
        self.db = db

# 3. DRY (Don't Repeat Yourself)
# Avoid duplication.
# Bad
price = 100
tax = price * 0.18

item2 = 200
tax2 = item2 * 0.18

# Good
def calculate_tax(price):
    return price * 0.18

# 4. KISS (Keep It Simple, Stupid)
# Choose the simplest solution that works.
# Overcomplicated
def is_even(num):
    return True if num % 2 == 0 else False
# Simple
def is_even(num):
    return num % 2 == 0

# 5. Design Patterns
# Reusable solutions to common programming problems.

# Creational Patterns
# Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory
class Car:
    pass

class Bike:
    pass


def vehicle_factory(vehicle_type):
    if vehicle_type == "car":
        return Car()
    return Bike()

# Structural Patterns
# Adapter
class Adapter:
    def __init__(self, obj):
        self.obj = obj

# Behavioral Patterns
# Observer
class Observer:
    def update(self):
        pass

# 6. Project Architecture
# - Defines overall structure of a project.
# project/
# │
# ├── app/
# ├── models/
# ├── services/
# ├── controllers/
# ├── tests/
# ├── docs/
# └── requirements.txt

# Benefits:
# - Scalability
# - Maintainability
# - Team collaboration

# 7. Layered Architecture
# - Separates application into layers.
# Presentation Layer
# ↓
# Business Layer
# ↓
# Data Access Layer
# ↓
# Database

# Presentation
user_controller()

# Business
user_service()

# Data
user_repository()

# Advantages
# Easy testing
# Better organization
# Loose coupling

# 8. Dependency Injection (DI)
# Instead of creating dependencies inside classes, inject them.
# Without DI
class UserService:
    def __init__(self):
        self.db = Database()
# With DI
class UserService:
    def __init__(self, db):
        self.db = db
# Usage:
db = Database()
service = UserService(db)
# Benefits:
# Easier testing
# Flexible code
# Loose coupling

# 9. Error Handling Strategy
# - Handle failures gracefully.
# Basic Example
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")
# Best Practices
# ✅ Catch specific exceptions
# ✅ Log errors
# ✅ Don't hide exceptions
# ✅ Provide meaningful messages
import logging

try:
    value = int(input())
except ValueError:
    logging.error("Invalid number")

# 10. Code Reviews
# - Process of checking code written by others.
# Goals
# - Find bugs
# - Improve quality
# - Share knowledge
# - Maintain coding standards
# Checklist
# - Code readability
# - Naming conventions
# - Error handling
# - Performance
# - Security issues
# - Test coverage

# 11. Git
# Version Control System.
# Common Commands
# Initialize Repository: git init
# Check Status: git status
# Add Files: git add .
# Commit: git commit -m "Initial commit"
# Push: git push origin main
# Pull: git pull origin main
# Create Branch: git checkout -b feature-login
# Merge: git merge feature-login

# Typical Workflow
# Create Branch
#       ↓
# Make Changes
#       ↓
# Commit
#       ↓
# Push
#       ↓
# Pull Request
#       ↓
# Code Review
#       ↓
# Merge

# 12. Documentation
# Documentation explains how software works.
# Types
# - User Documentation
# - Developer Documentation
# - Technical Documentation
# - Deployment Documentation

# # Project Name
#
# ## Installation
#
# pip install -r requirements.txt
#
# ## Run
#
# python app.py

# Good Documentation
# ✅ Clear
# ✅ Updated
# ✅ Easy to understand

# 13. API Documentation
# - Describes how APIs are used.
# Important Sections
# - Endpoint URL
# - Request Method
# - Parameters
# - Request Body
# - Response
# - Status Codes
# - Authentication

# Get User: GET /api/users/1
# Response:
# {
#   "id": 1,
#   "name": "Aman"
# }

# Status Codes
# 200 OK
# 201 Created
# 400 Bad Request
# 401 Unauthorized
# 404 Not Found
# 500 Internal Server Error

# Popular Tools
# Swagger / OpenAPI
# Postman
# ReDoc
# FastAPI Auto Docs

# Interview Questions
# Beginner
# What is Clean Code?
# What is DRY?
# Explain KISS.
# What are SOLID principles?
# What is code review?

# Intermediate
# Difference between DRY and KISS?
# What is Dependency Injection?
# Explain Layered Architecture.
# Why use design patterns?
# What is Git branching?

# Advanced
# Explain all SOLID principles with examples.
# When should Singleton not be used?
# How does Dependency Injection improve testability?
# Difference between Monolithic and Microservices architecture?
# How would you design a scalable REST API?

# Revision Notes
# Clean Code → Readable & maintainable code
# SOLID → Better object-oriented design
# DRY → Avoid duplication
# KISS → Keep solutions simple
# Design Patterns → Reusable solutions
# Architecture → Project structure
# Layered Architecture → Separation of concerns
# Dependency Injection → Inject dependencies
# Error Handling → Graceful failure
# Code Reviews → Improve quality
# Git → Version control
# Documentation → Explain software
# API Documentation → Explain API usage

# This topic is highly important for interviews and real-world development because it connects coding skills with professional software development practices.