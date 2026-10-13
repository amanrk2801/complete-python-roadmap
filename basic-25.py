# 43. Type Hints in Python
# Type hints are used to specify the expected data type of variables, function parameters, and return values. They improve code readability, IDE support, autocomplete, and static type checking.
# - Type hints do not enforce types at runtime. They are mainly for developers and tools like mypy.

# 1. Type Annotations
# Syntax: variable_name: data_type = value
# Example:
age: int = 25
name: str = "Aman"
salary: float = 50000.50

print(age)
print(name)
print(salary)

# 2. int
# - Represents integer values.
num: int = 100

def square(n: int) -> int:
    return n * n

print(square(5)) # 25

# 3. str
# - Represents text/string values.
name: str = "Python"

def greet(user: str) -> str:
    return f"Hello {user}"

print(greet("Aman"))
# Output: Hello Aman

# 4. list
# For lists.
# Traditional Syntax
from typing import List
numbers: List[int] = [1, 2, 3]
# Modern Syntax (Python 3.9+)
numbers: list[int] = [1, 2, 3]
# Example:
def total(nums: list[int]) -> int:
    return sum(nums)

print(total([10, 20, 30])) # 60

# 5. dict
# - For dictionaries.
student: dict[str, int] = {
    "Math": 90,
    "Science": 85
}

print(student)

# Function Example:
def get_marks() -> dict[str, int]:
    return {
        "Math": 95,
        "English": 88
    }

# 6. Optional
# - Used when a value can be a type or None.
from typing import Optional

def get_name(name: Optional[str]) -> str:
    if name is None:
        return "Guest"
    return name

print(get_name("Aman"))
print(get_name(None))
# Output:
# Aman
# Guest
# Equivalent Modern Syntax:
# def get_name(name: str | None) -> str:
#     ...

# 7. Union
# - A value can be one of multiple types.
from typing import Union

def display(value: Union[int, str]) -> None:
    print(value)

display(100)
display("Python")
# Modern Syntax:
def display(value: int | str) -> None:
    print(value)

# 8. Any
# - Accepts any data type.
from typing import Any

def show(data: Any) -> None:
    print(data)

show(10)
show("Python")
show([1, 2, 3])
# Use sparingly because it removes type-checking benefits.

# 9. Literal
# - Restricts a value to specific choices.
from typing import Literal

def set_mode(mode: Literal["read", "write"]) -> None:
    print(mode)

set_mode("read")
# Valid:
# set_mode("read")
# set_mode("write")
# Invalid:
# set_mode("delete")
# (Type checker will show an error.)

# 10. TypeAlias
# - Creates custom type aliases.
from typing import TypeAlias

Vector: TypeAlias = list[int]

data: Vector = [1, 2, 3]
print(data)
# Example:
UserId: TypeAlias = int
user: UserId = 101

# 11. Generic Types
# - Generics allow reusable code with different types.
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))
print(first_item(["A", "B", "C"]))

# Output:
# 1
# A

# 12. TypedDict
# - Provides type hints for dictionary keys.
from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    marks: float

student: Student = {
    "name": "Aman",
    "age": 22,
    "marks": 89.5
}

print(student)
# Benefits:
# student["name"]   # str
# student["age"]    # int

# 13. Protocol
# - Defines required methods (Duck Typing).
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        ...

class Human:
    def speak(self) -> str:
        return "Hello"

class Robot:
    def speak(self) -> str:
        return "Beep"

def talk(obj: Speaker) -> None:
    print(obj.speak())

talk(Human())
talk(Robot())

# Output:
# Hello
# Beep

# 14. Callable
# - Used for functions as parameters.
from typing import Callable

def operate(
    func: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

print(operate(add, 5, 3)) # 8

# Modern Syntax (Recommended)
# - Python 3.10+ supports simpler syntax:
def add(a: int, b: int) -> int:
    return a + b

def show(value: int | str) -> None:
    print(value)

def get_name(name: str | None) -> str:
    return name or "Guest"

numbers: list[int] = [1, 2, 3]
student: dict[str, int] = {"Math": 95}

# Interview Questions
# 1. Are type hints enforced at runtime? - NO
def add(a: int, b: int) -> int:
    return a + b
print(add("10", "20")) # 1020
# Python runs it without error because type hints are not enforced automatically.

# 2. Difference between Any and Union? - Any
# Accepts absolutely any type.
# Union[int, str]
# Accepts only int or str.

# 3. Difference between Optional[str] and str? - str
# Only string values.
# Optional[str]
# String or None.

# 4. What is a Generic?
# A way to write reusable functions/classes that work with multiple data types while preserving type safety.

# Quick Summary
# int                 # Integer
# str                 # String
# list[int]           # List of integers
# dict[str, int]      # Dictionary
# Optional[str]       # String or None
# int | str           # Union
# Any                 # Any type
# Literal             # Fixed values
# TypeAlias           # Custom type
# TypeVar             # Generics
# TypedDict           # Typed dictionaries
# Protocol            # Duck typing
# Callable            # Function type

# Most Commonly Used in Real Projects
# int
# str
# float
# bool
# list[T]
# dict[K, V]
# Optional
# Union (|)
# TypedDict
# Callable

# -------------------------------------------- #
# 44. Dataclasses (Python)