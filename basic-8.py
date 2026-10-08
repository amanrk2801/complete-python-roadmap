# 13. Functions in Python
# Functions are reusable blocks of code that perform a specific task. They help make programs organized, readable, and reusable.

# 1. Defining Functions
# Functions are created using the def keyword.
# Syntax
# def function_name():
#     # code

# Here, greet() is a function definition.
def greet():
    print("Hello")

# 2. Calling Functions: After defining a function, we need to call it to execute its code.
def greet():
    print("Hello")
greet()

# 3. Parameters: Parameters are variables listed in the function definition.
def greet(name):
    print("Hello", name)
# Here, name is a parameter.

# 4. Arguments: Arguments are actual values passed to a function when calling it.
def greet(name):
    print("Hello", name)
greet("Aman") # Hello, Aman # Here, "Aman" is an argument.

# 5. Return Values: The return keyword sends a value back from a function.
def add(a, b):
    return a + b
result = add(10, 20)
print(result) # 30

# 6. Local Variables: Variables created inside a function are local variables.
def test():
    x = 10
    print(x)
test() # 10
# Note: Trying to access x outside the function will cause an error.
# print(x) # NameError: name 'x' is not defined

# 7. Global Variables: Variables defined outside all functions are global variables.
x = 100
def display():
    print(x)
display() # 100

# 8. Function Scope: Scope determines where a variable can be accessed.
a = 50
def test():
    b = 10
    print(a)  # accessible
    print(b)  # accessible
test() # 50 10
# print(b)  # Error

# Global variable → accessible everywhere.
# Local variable → accessible only inside the function.

# 9. Default Arguments: Default values can be assigned to parameters.
def greet(name="Guest"):
    print("Hello", name)
greet() # Hello Guest
greet("Aman") # Hello Aman

# 10. Keyword Arguments: Arguments passed using parameter names.
def student(name, age):
    print(name, age)
student(age=22, name="Aman") # Aman 22
# Order does not matter with keyword arguments.

# 11. Positional Arguments: Arguments are assigned according to their position.
def student(name, age):
    print(name, age)
student("Aman", 22) # Aman 22
# Order matters.

# 12. *args
# Used to pass multiple positional arguments.
def add(*args):
    print(args)
add(1, 2, 3, 4) # (1, 2, 3, 4)
# Sum Example
def add(*numbers):
    return sum(numbers)
print(add(10, 20, 30)) # 60

# 13. **kwargs
# Used to pass multiple keyword arguments.
def display(**kwargs):
    print(kwargs)
display(name="Aman", age=22) # {'name': 'Aman', 'age': 22}
# Loop Example
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
display(name="Aman", city="Nagpur") # name Aman, city Nagpur

# 14. Keyword-Only Arguments
# Parameters after * must be passed using keywords.
def student(name, *, age):
    print(name, age)
student("Aman", age=22) # Aman 22

# ❌ Error
def student(name, *, age):
    print(name, age)
# student("Aman", 22) # TypeError: student() takes 1 positional argument but 2 were given

# 15. Positional-Only Arguments
# Parameters before / must be passed positionally.
def student(name, /, age):
    print(name, age)
student("Aman", 22) # Aman 22
# ❌ Error
def student(name, /, age):
    print(name, age)
# student(name="Aman", age=22) # TypeError: student() got some positional-only arguments passed as keyword arguments: 'name'

# 16. Multiple Return Values
# Python can return multiple values separated by commas.
# Example
def calculate(a, b):
    return a + b, a - b
sum_result, diff_result = calculate(10, 5)
print(sum_result) # 15
print(diff_result) # 5

# 17. Docstrings
# Docstrings are used to describe what a function does.
# Example
def add(a, b):
    """
    Returns sum of two numbers.
    """
    return a + b
print(add.__doc__) # Returns sum of two numbers.

# 18. Function Annotations: Annotations provide type hints.
# Example
def add(a: int, b: int) -> int:
    return a + b
print(add(10, 20)) # 30
# Type hints improve readability and IDE support.

# 19. Recursion: A function calling itself is called recursion.
# Example: Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) # 120
# Flow
# factorial(5) \
#     = 5 * factorial(4) \
#     = 5 * 4 * factorial(3) \
#     = 5 * 4 * 3 * factorial(2) \
#     = 5 * 4 * 3 * 2 * factorial(1) \
#     = 5 * 4 * 3 * 2 * 1 \
#     = 120

# Interview Questions
# Q1. Difference between Parameter and Argument?
def add(a, b):  # parameters
    return a + b
add(10, 20)     # arguments
# Parameters → Function definition variables.
# Arguments → Actual values passed.

# Q2. Difference between Local and Global Variable?
x = 100  # global
def test():
    y = 10  # local
# Local → Exists inside function.
# Global → Exists throughout program.

# Q3. Difference between *args and **kwargs?
def demo(*args, **kwargs):
    print(args)
    print(kwargs)
# *args → Multiple positional arguments → tuple.
# **kwargs → Multiple keyword arguments → dictionary.

# Q4. Why use functions?
# - Code reusability
# - Better readability
# - Easier debugging
# - Modular programming
# - Less code duplication

# Practice Programs
# 1. Create a function to find the square of a number.
# 2. Create a function to check even/odd.
# 3. Create a function to find the largest of two numbers.
# 4. Create a function using default arguments.
# 5. Create a function using *args to calculate sum.
# 6. Create a recursive function for factorial.
# 7. Create a recursive function for Fibonacci series.

# ✅ Mastering Functions is one of the most important topics in Python because almost every real-world project uses functions extensively.

# ------------------------------------------------------------------ #

# 14. Scope & Namespace in Python
# Scope determines where a variable can be accessed, while a Namespace is a place where variable names are stored.

# 1. LEGB Rule: Python searches for variables in the following order:
# L → E → G → B
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in
x = "Global"
def show():
    x = "Local"
    print(x)
show() # Local
print(x) # Global
# Python finds x in the local scope first.

# 2. Local Scope: Variables created inside a function belong to the local scope.
# ✅ Accessible only inside the function.
def greet():
    name = "Aman"   # Local variable
    print(name)
greet() # Aman
# ❌ Error:
def greet():
    name = "Aman"
greet()
# print(name) # NameError: name 'name' is not defined

# 3. Enclosing Scope: Occurs when a function is inside another function.
def outer():
    message = "Hello"
    def inner():
        print(message)
    inner()
outer() # Hello
# message belongs to the enclosing scope of inner().

# 4. Global Scope: Variables defined outside all functions.
city = "Mumbai"
def display():
    print(city)
display() # Mumbai
# Global variables can be read inside functions.

# Modifying Global Variables
# Without global keyword:
# count = 10
# def increase():
#     count = count + 1
# increase() # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
# Because Python treats count as a local variable.

# 5. Built-in Scope: Contains Python's predefined names.
# Examples:
# print()
# len()
# sum()
# max()
# min()
# type()
numbers = [10, 20, 30]
print(len(numbers)) # 3 : Python finds len() in the built-in scope.

# 6. global Keyword: Used to modify a global variable inside a function.
count = 0
def increment():
    global count
    count += 1
increment()
print(count) # 1
# How it works
x = 5
def change():
    global x
    x = 100
change()
print(x) # 100

# 7. nonlocal Keyword: Used to modify a variable in the enclosing scope.
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
outer() # 20

# Without nonlocal
def outer():
    x = 10
    def inner():
        x = 20
    inner()
    print(x)
outer() # 10
# Because a new local variable is created inside inner().

# 8. Namespace
# A namespace is a dictionary-like structure that maps names to objects.
name = "Aman"
age = 22
# Namespace
{
    "name": "Aman",
    "age": 22
}
# Types of Namespaces
# Built-in Namespace
# - print
# - len
# - sum
# Global Namespace
x = 10
y = 20
# Local Namespace
def test():
    z = 30
# You can view a namespace using:
print(globals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020C2793A390>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Aman\\PycharmProjects\\WelcomeScreen\\basic-8.py', '__cached__': None, 'greet': <function greet at 0x0000020C27B40A90>, 'add': <function add at 0x0000020C29D10BF0>, 'result': 30, 'test': <function test at 0x0000020C29D10EB0>, 'x': 10, 'display': <function display at 0x0000020C29D10D50>, 'a': 50, 'student': <function student at 0x0000020C27ECFCC0>, 'calculate': <function calculate at 0x0000020C27993530>, 'sum_result': 15, 'diff_result': 5, 'factorial': <function factorial at 0x0000020C27ECFE20>, 'demo': <function demo at 0x0000020C27ECFC10>, 'show': <function show at 0x0000020C29D10B40>, 'outer': <function outer at 0x0000020C29D10CA0>, 'city': 'Mumbai', 'numbers': [10, 20, 30], 'count': 1, 'increment': <function increment at 0x0000020C27ECFB60>, 'change': <function change at 0x0000020C29D10E00>, 'name': 'Aman', 'age': 22, 'y': 20}
print(locals()) # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020C2793A390>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\Aman\\PycharmProjects\\WelcomeScreen\\basic-8.py', '__cached__': None, 'greet': <function greet at 0x0000020C27B40A90>, 'add': <function add at 0x0000020C29D10BF0>, 'result': 30, 'test': <function test at 0x0000020C29D10EB0>, 'x': 10, 'display': <function display at 0x0000020C29D10D50>, 'a': 50, 'student': <function student at 0x0000020C27ECFCC0>, 'calculate': <function calculate at 0x0000020C27993530>, 'sum_result': 15, 'diff_result': 5, 'factorial': <function factorial at 0x0000020C27ECFE20>, 'demo': <function demo at 0x0000020C27ECFC10>, 'show': <function show at 0x0000020C29D10B40>, 'outer': <function outer at 0x0000020C29D10CA0>, 'city': 'Mumbai', 'numbers': [10, 20, 30], 'count': 1, 'increment': <function increment at 0x0000020C27ECFB60>, 'change': <function change at 0x0000020C29D10E00>, 'name': 'Aman', 'age': 22, 'y': 20}

# 9. Variable Lifetime
# The lifetime of a variable is the period during which it exists in memory.
# Local Variable Lifetime
def demo():
    x = 10
    print(x)
demo() # 10
# After the function finishes, x is destroyed.

# Global Variable Lifetime
x = 100
def show():
    print(x)
show() # 100
# x exists until the program ends.

# Complete LEGB Example
x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print(x)
    inner()
outer() # Local
print(x) # Global

# Search Process
# Inside inner():
# 1. Check Local → "Local" ✅ Found
# 2. Enclosing → Skip
# 3. Global → Skip
# 4. Built-in → Skip

# Interview Questions
# Q1: What is LEGB?
# Local → Enclosing → Global → Built-in, the order Python uses to look up variable names.

# Q2: Difference between global and nonlocal?
# global    # modifies global variable
# nonlocal  # modifies enclosing scope variable

# Q3: What is a namespace?
# A container that stores variable names and their corresponding objects.

# Q4: When are local variables destroyed?
# When the function execution ends.

# Q5: What is the scope of a variable?
# The region of the program where that variable can be accessed.

# Quick Revision
# Scope = Where a variable can be accessed.
#
# LEGB Rule:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in
#
# global   → Modify global variable
# nonlocal → Modify enclosing variable
#
# Namespace = Collection of names and objects
#
# Local variable lifetime:
# Function starts → Variable created
# Function ends   → Variable destroyed
#
# Global variable lifetime:
# Program starts → Variable created
# Program ends   → Variable destroyed

