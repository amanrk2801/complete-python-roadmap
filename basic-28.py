# 49. Environment & Configuration in Python
# Environment & Configuration is about managing application settings, secrets, and behavior across different environments without hardcoding values in your code.

# 1. Environment Variables
# Environment variables are key-value pairs stored outside your Python code.
# Why use them?
# Store configuration outside code
# Keep secrets secure
# Change behavior without modifying source code

# Setting Environment Variables
# Linux/macOS
# export DB_HOST=localhost
# export DB_PORT=5432
# Windows CMD
# set DB_HOST=localhost
# Windows PowerShell
# $env:DB_HOST="localhost"

# Reading in Python
import os

host = os.getenv("DB_HOST")
print(host)
# Output: localhost

# 2. .env Files
# - A .env file stores environment variables in a simple text format.
# .env
# DB_HOST=localhost
# DB_USER=admin
# DB_PASSWORD=secret123
# DEBUG=True

# Install python-dotenv
# pip install python-dotenv

# Load .env
# from dotenv import load_dotenv
# import os

# load_dotenv()

print(os.getenv("DB_HOST"))
print(os.getenv("DB_USER"))
# Output:
# localhost
# admin

# Never Commit
# Add to .gitignore
# .env
# Because it may contain:
# API keys
# Database passwords
# Tokens

# 3. The os Module
# - The os module helps interact with the operating system.

# Useful Functions
# Current Working Directory
import os
print(os.getcwd())

# Environment Variables
import os
print(os.environ["USER"])

# Safe Access
import os
print(os.getenv("PORT", "8000"))
# Output: 8000

# Create Directory
import os
os.mkdir("data")

# 4. The sys Module
# - Provides access to Python runtime information.
# Command Line Arguments
import sys
print(sys.argv)
# Run: python app.py hello world
# Output: ['app.py', 'hello', 'world']

# Python Version
import sys
print(sys.version)

# Exit Program
import sys
sys.exit()

# 5. Configuration Files
# - Instead of hardcoding values:
# ❌ Bad
host = "localhost"
port = 5432
# ✅ Better
# Store in config file
# host=localhost
# port=5432

# Benefits:
# Easier updates
# Cleaner code
# Environment-specific settings

# 6. configparser Module
# - Used for reading INI configuration files.
# config.ini
[database]
host = localhost
port = 5432
user = admin

[app]
debug = true

# Reading Config
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config["database"]["host"]
port = config["database"]["port"]

print(host)
print(port)

# Output:
# localhost
# 5432

# Writing Config
import configparser

config = configparser.ConfigParser()

config["app"] = {
    "debug": "true",
    "port": "8000"
}

with open("config.ini", "w") as f:
    config.write(f)

# 7. Secrets Management
# Secrets include:
# Database passwords
# API keys
# JWT secrets
# Access tokens

# Wrong Way
# API_KEY = "abcd1234"
# Better
# import os
# API_KEY = os.getenv("API_KEY")

# Best Practices
# ✅ Use environment variables
# ✅ Use secret managers
# AWS Secrets Manager
# Azure Key Vault
# HashiCorp Vault
# ✅ Keep secrets out of Git
# .env
# *.pem
# secrets.json
# ❌ Never hardcode passwords

# 8. Different Environments
# - Applications typically run in multiple environments.
# Development
#     ↓
# Testing
#     ↓
# Staging
#     ↓
# Production

# Development Environment
# Used by developers.
# Characteristics:
# - Debug mode ON
# - Local database
# - Frequent code changes
# DEBUG=True
# DB_NAME=dev_db

# Testing Environment
# - Used for automated tests.
# Characteristics:
# - Isolated database
# - Mock services
# - Temporary data
DEBUG=True
DB_NAME=test_db

# Staging Environment
# Production-like environment before release.
# Characteristics:
# - Real infrastructure
# - Final testing
# - Client validation
# Example:
# DEBUG=False
# DB_NAME=staging_db

# Production Environment
# Live application used by customers.
# Characteristics:
# - Debug OFF
# - Secure settings
# - Monitoring enabled
# Example:
# DEBUG=False
# DB_NAME=prod_db

# Example Project Structure
# my_project/
# │
# ├── app.py
# ├── .env
# ├── config.ini
# ├── requirements.txt
# │
# └── settings.py

# settings.py
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG") == "True"

# app.py
from settings import DATABASE_URL, DEBUG

print(DATABASE_URL)
print(DEBUG)

# Interview Questions
# Q1. Why use environment variables?
# To store configuration and secrets outside source code.

# Q2. Difference between os.environ and os.getenv()?
# os.environ["KEY"]
# - Raises KeyError if missing.
# os.getenv("KEY")
# - Returns None or default value.

# Q3. Why shouldn't secrets be hardcoded?
# - Because source code may be shared, pushed to Git, or exposed publicly.

# Q4. What is a .env file?
# - A file that stores environment variables in key-value format.

# Q5. What is the purpose of configparser?
# To read and write INI-style configuration files.

# Q6. What is the difference between Staging and Production?
# Staging: Pre-production testing environment.
# Production: Live environment used by customers.

# Quick Revision
# Environment Variables -> External settings
#
# .env -> Stores variables locally
#
# os -> OS interaction and env variables
#
# sys -> Python runtime and arguments
#
# configparser -> Read/write INI files
#
# Secrets -> Passwords, tokens, keys
#
# Development -> Build features
#
# Testing -> Run tests
#
# Staging -> Final verification
#
# Production -> Live system

# This topic is very important in real-world Python projects, especially when working with Flask, Django, FastAPI, Docker, Kubernetes, CI/CD pipelines, and cloud deployments.

# ------------------------------------------------ #
# 50. CLI Applications (Command Line Interface)
# - A CLI Application is a program that runs in the terminal and accepts user input through commands, arguments, and flags.
# python app.py hello Aman
# Here:
# python → command
# app.py → script
# hello → argument
# Aman → value

# 1. sys.argv
# - sys.argv is used to access command-line arguments directly.
import sys
print(sys.argv)
# Run: python app.py hello world
# Output: ['app.py', 'hello', 'world']
# Access arguments:
import sys

name = sys.argv[1]
print("Hello", name)
# Run: python app.py Aman
# Output: Hello Aman

# Limitation
# No validation
# Hard to manage many arguments

# 2. argparse
# Python's built-in library for CLI applications.
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print("Hello", args.name)

# Run: python app.py Aman
# Output: Hello Aman

# Multiple Arguments
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age", type=int)

args = parser.parse_args()

print(args.name)
print(args.age)

# Run: python app.py Aman 24
# Output:
# Aman
# 24

# 3. click
# - A popular third-party package.
# Install: pip install click
import click

@click.command()
@click.argument("name")
def hello(name):
    click.echo(f"Hello {name}")

hello()
# Run: python app.py Aman
# Output: Hello Aman

# Multiple Commands
import click

@click.group()
def cli():
    pass

@cli.command()
def start():
    print("Starting...")

@cli.command()
def stop():
    print("Stopping...")

cli()

# Run: python app.py start
# Output: Starting...

# 4. typer
# - Modern CLI framework built on Click.
# Install: pip install typer
import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

app()
# Run: python app.py hello Aman
# Output: Hello Aman
# Benefits
# - Uses type hints
# - Auto help generation
# - Easy to use

# 5. CLI Commands
# - A CLI tool can have multiple commands.
# git init
# git add .
# git commit -m "first commit"

# Here:
# git → application
# init, add, commit → commands

# Custom example with Typer:
import typer

app = typer.Typer()

@app.command()
def start():
    print("Server started")

@app.command()
def stop():
    print("Server stopped")

app()

# Run:
# python app.py start
# python app.py stop

# 6. Flags
# - Flags modify command behavior.
# python app.py --verbose
# Using argparse:
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--verbose",
    action="store_true"
)

args = parser.parse_args()

if args.verbose:
    print("Verbose mode enabled")

# Run: python app.py --verbose
# Output: Verbose mode enabled

# Flag with Value
# parser.add_argument("--port", type=int)
# Run: python app.py --port 8080

# 7. Arguments
# - Arguments are values passed to a command.
# python app.py Aman
# Code:
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)

# Output: Aman

# Positional vs Optional Arguments
# Positional: parser.add_argument("name")
# Must be supplied: python app.py Aman
# Optional: parser.add_argument("--name")
# Run: python app.py --name Aman

# 8. Interactive CLI
# - Interactive CLIs ask users for input during execution.
# name = input("Enter name: ")
# print("Hello", name)
# Output:
# Enter name: Aman
# Hello Aman

# Menu-Based CLI
while True:
    print("\n1. Add")
    print("2. View")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Adding...")

    elif choice == "2":
        print("Viewing...")

    elif choice == "3":
        print("Bye")
        break

    else:
        print("Invalid choice")

# Mini Project: Todo CLI
tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        break

# Interview Questions
# 1. What is CLI?
# A program that is operated through terminal commands instead of a graphical interface.

# 2. Difference between argument and flag?
# Argument: python app.py Aman
# Flag: python app.py --verbose

# 3. Why use argparse instead of sys.argv?
# Validation
# Help messages
# Type conversion
# Better maintainability

# 4. Click vs Typer?
# Click - Typer
# Older - Newer
# More manual - Uses type hints
# Flexible - Easier

# 5. What does action="store_true" do?
# Creates a boolean flag.
# python app.py --debug
# Result: True

# Practice Tasks
# Create a CLI that adds two numbers using sys.argv.
# Build a calculator with argparse.
# Make a user management CLI using Click.
# Create a Typer app with create, delete, and list commands.
# Build a menu-driven Student Management System using an interactive CLI.