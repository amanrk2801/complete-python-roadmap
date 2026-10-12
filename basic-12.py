# 20. Packages in Python
# - A package is a way of organizing related Python modules into directories. Packages help keep large projects structured and manageable.

# 1. Creating Packages
# - A package is simply a folder containing Python modules and usually an __init__.py file.
# my_package/
# │
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py

# math_utils.py
def add(a, b):
    return a + b
# string_utils.py
def greet(name):
    return f"Hello, {name}"
# Using the package:
from my_package.math_utils import add
print(add(10, 20)) # 30

# 2. Package Structure
# Typical structure:
# project/
# │
# ├── main.py
# │
# └── my_package/
#     ├── __init__.py
#     ├── module1.py
#     ├── module2.py
#     └── module3.py
# project → main application
# my_package → package
# module1.py, module2.py → modules

# 3. __init__.py
# - This file tells Python that the directory should be treated as a package.
# Example:
# __init__.py
print("Package initialized")

# When package is imported:
import my_package
# Output: Package initialized

# You can also expose functions:
from .math_utils import add
# Now:
from my_package import add
print(add(5, 5))

# 4. Nested Packages - Packages can contain sub-packages.
# Structure:
# company/
# │
# ├── __init__.py
# │
# └── employees/
#     ├── __init__.py
#     └── manager.py
# manager.py
def show():
    print("Manager Details")
# Usage:
from company.employees.manager import show
show()
# Output: Manager Details

# 5. Relative Imports - Import modules using dots (.).
# Structure:
# mypackage/
# │
# ├── __init__.py
# ├── module1.py
# └── module2.py
# module1.py
def greet():
    print("Hello")
# module2.py
from .module1 import greet
greet()

# Symbols:
# .      # current package
# ..     # parent package
# ...    # grandparent package

# Example: from ..utils import helper

# 6. Absolute Imports - Import using the complete package path.
from mypackage.module1 import greet
greet()
# Advantages:
# - Easier to read
# - Less confusing
# - Preferred in large projects

# 7. Installing Packages
# - Packages can be installed from PyPI using pip.
# Syntax: pip install package_name
# Example: pip install requests
# Check installation:
import requests
print(requests.__version__)

# 8. pip
# pip = Package Installer for Python.
# Common commands:
# Install package : pip install numpy
# Uninstall package : pip uninstall numpy
# Upgrade package : pip install --upgrade numpy
# List installed packages : pip list
# Show package details : pip show numpy
# Install specific version : pip install numpy==1.26.4
# Install from requirements file : pip install -r requirements.txt
# requirements.txt
#   numpy==1.26.4
#   pandas==2.2.3
#   requests==2.32.3

# 9. PyPI
# - PyPI (Python Package Index) is the official repository of Python packages.
# Website: https://pypi.org
# Popular packages available on PyPI:
# Package -> Purpose
# numpy -> Numerical computing
# pandas -> Data analysis
# requests -> HTTP requests
# matplotlib -> Data visualization
# flask -> Web applications
# django -> Full-stack web development

# Install any package from PyPI: pip install pandas

# Interview Questions
# Q1. What is a package in Python?
# - A package is a directory containing related modules and an __init__.py file.

# Q2. Difference between module and package?
# - Module: Single .py file
# calculator.py
# - Package: Collection of modules
# utils/
# ├── module1.py
# ├── module2.py
# └── __init__.py

# Q3. What is __init__.py?
# - It initializes a package and allows Python to recognize the directory as a package.

# Q4. Difference between relative and absolute import?
# Relative: from .module1 import greet
# Absolute: from mypackage.module1 import greet

# Q5. What is PyPI?
# - PyPI is the official online repository for Python packages.

# Q6. What is pip?
# - pip is Python's package manager used to install, update, and remove packages.

# Quick Revision
# Package = Folder containing modules
#
# __init__.py → Makes folder a package
#
# Nested Package:
# package/
#     subpackage/
#         module.py
#
# Relative Import:
# from .module import func
#
# Absolute Import:
# from package.module import func
#
# pip install package_name
# pip uninstall package_name
# pip list
# pip show package_name
#
# PyPI = Official Python package repository

# --------------------------------------------- #

# 21. Virtual Environments (Python)
# 1. Why Virtual Environments?
# - A virtual environment is an isolated Python environment that has its own:
# Python interpreter
# Installed packages
# Dependencies

# Problem Without Virtual Environments
# Project A needs: Django==4.2
# Project B needs: Django==5.0
# Installing both globally can cause conflicts.

# Solution: Create separate environments:
# Project-A/
#  └── venv/
#
# Project-B/
#  └── venv/

# Each project can use different package versions independently.

# 2. venv - venv is Python's built-in module for creating virtual environments.
# Check Python version: python --version
# Create environment using: python -m venv venv
# Syntax: python -m venv <environment_name>
# Example: python -m venv myenv

# 3. Creating Environments
# Windows : python -m venv venv
# Directory structure:
# project/
# │
# ├── venv/
# ├── app.py
# └── requirements.txt

# Linux/macOS: python3 -m venv venv

# 4. Activating Environments
# - Windows (CMD): venv\Scripts\activate
# - Windows (PowerShell): .\venv\Scripts\Activate.ps1
# - Linux/macOS: source venv/bin/activate
# Active environment shows: (venv) C:\project>
# or : (venv) user@ubuntu:~$

# 5. Deactivating Environment
# To exit virtual environment: deactivate
# Prompt returns to normal: C:\project>

# 6. requirements.txt : Stores all project dependencies.
# requests==2.32.3
# numpy==2.1.0
# pandas==2.2.3
# Install packages from file: pip install -r requirements.txt
# Useful when sharing projects with others.

# 7. pip freeze: Displays installed packages and versions.
# - pip freeze
# Example output:
# numpy==2.1.0
# pandas==2.2.3
# requests==2.32.3
# Save to requirements file: pip freeze > requirements.txt
# Reinstall later: pip install -r requirements.txt

# 8. Dependency Management
# - Dependency management means tracking and controlling package versions.
# Install Package: pip install requests
# Install Specific Version: pip install requests==2.32.3
# Upgrade Package: pip install --upgrade requests
# Remove Package: pip uninstall requests
# View Installed Packages: pip list
# Check Dependencies: pip show requests

# Advanced Topics
# 1. Poetry - Poetry is a modern dependency and package management tool.
# Benefits:
# Creates virtual environments automatically
# Dependency resolution
# Package publishing
# Uses pyproject.toml
# Easier project management

# Install: pip install poetry
# Create project: poetry new myproject
# Install dependencies: poetry install
# Add package: poetry add requests
# Remove package: poetry remove requests
# Activate shell: poetry shell
# Show environment: poetry env info

# 2. pyproject.toml : Modern Python project configuration file.
# TOML file
# [project]
# name = "myproject"
# version = "0.1.0"
# description = "Sample project"
# dependencies = [
#     "requests",
#     "numpy"
# ]

# Used by:
# Poetry
# Hatch
# PDM
# uv
# Build tools

# Benefits:
# Central configuration file
# Package metadata
# Dependency management
# Build system configuration

# 3. uv : uv is a very fast Python package manager written in Rust.
# Features:
# Fast package installation
# Fast virtual environment creation
# Compatible with pip
# Dependency management
# Uses pyproject.toml

# Install: pip install uv
# Create environment: uv venv
# Activate:
# Windows : .venv\Scripts\activate
# Linux/macOS : source .venv/bin/activate

# Install package: uv pip install requests
# Install from requirements: uv pip install -r requirements.txt
# Run Python: uv run main.py

# Interview Questions
# Q1: Why use virtual environments?
# - To isolate project dependencies and avoid version conflicts.

# Q2: How do you create a virtual environment?
# - python -m venv venv

# Q3: How do you activate it in PowerShell?
# - .\venv\Scripts\Activate.ps1

# Q4: How do you deactivate it?
# - deactivate

# Q5: What is requirements.txt?
# - A file containing all project dependencies and versions.

# Q6: What does pip freeze do?
# - Lists installed packages and versions.

# Q7: Difference between pip and Poetry?
# pip -> Poetry
# Package installer -> Complete dependency manager
# Uses requirements.txt -> Uses pyproject.toml
# Manual dependency handling -> Automatic dependency resolution

# Q8: What is uv? : A high-performance Python package and environment manager written in Rust.

# Quick Revision
# # Create environment
# python -m venv venv
#
# # Activate (Windows)
# venv\Scripts\activate
#
# # Activate (Linux/macOS)
# source venv/bin/activate
#
# # Install package
# pip install requests
#
# # Save dependencies
# pip freeze > requirements.txt
#
# # Install dependencies
# pip install -r requirements.txt
#
# # Exit environment
# deactivate

# ✅ Key Point: In real-world Python development, every project should generally have its own virtual environment to keep dependencies isolated, reproducible, and conflict-free.