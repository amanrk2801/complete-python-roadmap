# 17. Exception Handling in Python
# - Exception Handling helps a program handle runtime errors gracefully without crashing.
# 1. Errors vs Exceptions
# Errors - Errors are serious problems that usually stop program execution.
# print("Hello" # SyntaxError: '(' was never closed
# Exceptions - Exceptions occur during execution and can be handled.
# num = int("abc") # ValueError: invalid literal for int()

# 2. try - The code that may cause an exception is written inside the try block.
try:
    num = int(input("Enter number: "))
    print(10 / num)
finally:
    print("Ok")

# 3. except - Handles the exception if it occurs.
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 4. else - Runs only when no exception occurs.
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result =", result)

# 5. finally - Always executes, whether an exception occurs or not.
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Program finished")

# 6. Multiple Exceptions - Handle different exceptions separately.
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions together
try:
    num = int(input())
    print(10 / num)
except (ValueError, ZeroDivisionError):
    print("Error occurred")

# 7. Nested Exception Handling - Using try-except inside another try.
try:
    num = int(input("Enter number: "))
    try:
        print(10 / num)
    except ZeroDivisionError:
        print("Division by zero")
except ValueError:
    print("Invalid input")

# 8. raise - Used to manually generate an exception.
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
print("Eligible")

# 9. Custom Exceptions - Creating your own exception type.
class InvalidAgeError(Exception):
    pass
age = 15
if age < 18:
    raise InvalidAgeError("Not eligible")
# Output: InvalidAgeError: Not eligible

# 10. Exception Hierarchy
# - All exceptions inherit from BaseException.
# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
#     ├── ArithmeticError
#     │   ├── ZeroDivisionError
#     │   └── OverflowError
#     │
#     ├── ValueError
#     ├── TypeError
#     ├── IndexError
#     ├── KeyError
#     ├── FileNotFoundError
#     └── AttributeError

# Example: print(10 / 0)
# ZeroDivisionError → ArithmeticError → Exception → BaseException

# 11. Creating Custom Exception Classes
# - Custom exception with constructor.
class BalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return f"Insufficient balance: {self.balance}"
balance = 500
if balance < 1000:
    raise BalanceError(balance)
# Output
# BalanceError: Insufficient balance: 500

# 12. assert - Used for debugging and testing assumptions.
# Syntax: assert condition, "Error message"
age = 15
assert age >= 18, "Age must be 18+"
# Output: AssertionError: Age must be 18+

# Example:
num = 10
assert num > 0
print("Positive number")
# Output: Positive number

# Complete Example
try:
    num = int(input("Enter number: "))

    assert num > 0, "Number must be positive"

    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

except AssertionError as e:
    print(e)

else:
    print("Result =", result)

finally:
    print("Execution completed")

# Interview Questions
# Q1. Difference between Error and Exception?
# - Error: Syntax mistakes or system-level issues.
# - Exception: Runtime problem that can be handled.

# Q2. Difference between except and finally?
# - except runs only when exception occurs.
# - finally always runs.

# Q3. Why use raise?
# - To manually throw an exception.

# Q4. Why use custom exceptions?
# - To create meaningful application-specific error messages.

# Q5. What is assert used for?
# - For debugging and checking assumptions during development.