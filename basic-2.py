### 3. Operators in Python
# Operators are special symbols that perform operations on variables and values.
# 1. Arithmetic Operators: Used for mathematical calculations.
a = 10
b = 3
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # floor division
print(a % b) # modulus(remainder)
print(a ** b) # power

# 2. Assignment Operators: Used to assign values to variables.
x = 10
x += 5   # x = x + 5
x -= 2   # x = x - 2
x *= 3   # x = x * 3
x /= 2   # x = x / 2
x //= 2   # x = x // 2
x %= 2   # x = x % 2
x **= 2   # x = x ** 2
print(x) # 1.0

# 3. Comparison Operators: Used to compare two values.
a = 10
b = 20
print(a == b)  # False
print(a != b)   # True
print(a > b)  # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

# 4. Logical Operators: Used to combine conditions.
age = 20
print(age > 18 and age < 60)
print(age > 18 or age < 10)
print(not(age > 18))

# 5. Bitwise Operators: Work on binary (bits).
a = 5      # 0101
b = 3      # 0011
print(a & b)   # AND: 1
print(a | b)   # OR: 7
print(a ^ b) # XOR: 6
print(~a) # NOT: -6
print(a << b) # LEFT SHIFT: 40
print(a >> b) # RIGHT SHIFT: 0

# 6. Membership Operators: Check whether a value exists in a sequence.
# in: Returns True if value exists.
nums = [1, 2, 3, 4]
print(3 in nums) # True

# not in: Returns True if value does not exist.
nums = [1, 2, 3, 4]
print(5 not in nums) # True

# 7. Identity Operators: Check whether two variables refer to the same object in memory.
# is
a = [1, 2]
b = a
print(a is b) # True

# is not
a = [1, 2]
b = [1, 2]
print(a is not b) # True

# Difference Between == and is
a = [1, 2]
b = [1, 2]
print(a == b)  # True (values same) # == → compares values
print(a is b)  # False (different objects) # is → compares memory location (object identity)

# 8. Operator Precedence: Determines which operation is performed first.
result = 10 + 5 * 2
print(result) # 20: Because * has higher precedence than +.

# 9. Chained Comparisons
# Python allows multiple comparisons in a single statement.
x = 15
print(10 < x < 20) # True

# Interview Question
# What is the difference between Membership and Identity operators?
# Membership Operators (in, not in)
# Check whether a value exists in a collection.
3 in [1, 2, 3]
# True

# Identity Operators (is, is not)
# Check whether two variables point to the same object.
a = [1, 2]
b = a
print(a is b) # True

# Easy Memory Trick:
# in → "Is the value inside the collection?"
# is → "Is it the same object in memory?" ✅

# ------------------------------------------------------- #

### 4. Input & Output in Python
# Input and Output (I/O) allows a program to interact with users and display results.
# 1. print(): Used to display output on the screen.
print("Hello World")
print(100)
print(True)
# Multiple Values
name = "Aman"
age = 25
print(name, age) # Aman 25
# Custom Separator
print("Python", "Java", "C++", sep=" | ") # Python | Java | C++
# Custom End Character
print("Hello", end=" ")
print("World") # Hello World

# 2. input(): Used to take input from the user.
name = input("Enter your name: ")
print("Hello", name)
# Important: input() always returns a string.
age = input("Enter age: ")
print(type(age)) # <class 'str'>
# To convert:
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

# 3. String Formatting: String formatting means inserting values into a string.
name = "Aman"
age = 25
print("My name is", name, "and age is", age) # My name is Aman and age is 25

# 4. f-Strings (Recommended): Introduced in Python 3.6. Fast and readable.
name = "Aman"
age = 25
print(f"My name is {name} and I am {age} years old.") # My name is Aman and I am 25 years old.
# Expressions Inside f-Strings
a = 10
b = 20
print(f"Sum = {a + b}") # Sum = 30
# Decimal Formatting
pi = 3.14159265
print(f"{pi:.2f}") # 3.14

# 5. format(): Another way to insert values into strings.
name = "Aman"
age = 25
print("My name is {} and age is {}".format(name, age)) # My name is Aman and age is 25
# Positional Arguments
print("{1} is older than {0}".format("Rahul", "Aman")) # Aman is older than Rahul
# Named Arguments
print("Name: {name}, Age: {age}".format(name="Aman", age=25)) # Name: Aman, Age: 25

# 6. % Formatting (Old Style): Older formatting method from C language.
name = "Aman"
age = 25
print("My name is %s and age is %d" % (name, age)) # My name is Aman and age is 25
# Common Specifiers
# %s -> string
# %d -> integer
# %f -> float
# %.2f -> float with 2 decimals places
price = 99.999
print("Price = %.2f" % price) # Price = 100.00

# 7. Escape Characters: Used to insert special characters into strings.
# \n -> New Line
# \t -> Tab
# \\ -> Backslash
# \' -> Single Quote
# \" -> Double Quote
print("Hello\nWorld")
print("Name\tAge")
print("He said \"Hello\"")

# 8. sys.stdin: Used for fast input, especially in coding competitions.
import sys
name = sys.stdin.readline()
print(name)
# Integer Input
import sys
n = int(sys.stdin.readline())
print(n)
# Multiple Integers
import sys
a, b = map(int, sys.stdin.readline().split())
print(a + b)

# 9. sys.stdout: Used for fast output.
import sys
sys.stdout.write("Hello World\n") # Hello World
# Difference from print()
import sys
sys.stdout.write("Python\n") # Python
print("Java") # Java
# print() is easier to use, while
# sys.stdout.write() is often used for faster output.

# Interview Questions
# Q1. What does input() return?: A string (str).
# Q2. Which string formatting method is recommended?: f-strings.
# Q3. Difference between print() and sys.stdout.write()?
# - print() automatically adds a newline.
# - sys.stdout.write() does not add a newline automatically.
# Q4. What is \n?: Escape character for a new line.
# Q5. What is the advantage of sys.stdin.readline()?: Faster input handling for large amounts of data.

# Quick Revision
# Input
name = input("Enter name: ")

# Output
print(name)

# f-string
print(f"Hello {name}")

# format()
print("Hello {}".format(name))

# % formatting
print("Hello %s" % name)

# Escape character
print("Hello\nWorld")

# Fast input
import sys
n = int(sys.stdin.readline())

# Fast output
sys.stdout.write(str(n))

# Best Modern Practice: Use input() for normal programs, print() for output, and f-strings for string formatting. Use sys.stdin and sys.stdout mainly in competitive programming and high-performance applications.

### 5. Conditional Statements: Conditional statements help a program make decisions based on conditions.
# 1. if Statement: Executes a block of code only if the condition is True.
age = 18
if age >= 18:
    print("You are eligible to vote")

# 2. elif Statement: Used to check multiple conditions.
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
# Only the first matching condition executes.

# 3. else Statement: Runs when all previous conditions are False.
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 4. Nested Conditions: An if statement inside another if.
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need a license")
else:
    print("Too young to drive")

# 5. Multiple Conditions: Using and, or, and not.
# and: Both conditions must be true.
age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible")
# or: At least one condition must be true.
weekend = False
holiday = True
if weekend or holiday:
    print("No office")
# not: Reverses a result.
logged_in = False
if not logged_in:
    print("Please login")

# 6. Ternary (Conditional) Expression
# Short form of if-else.
# Normal
age = 20
if age >= 18:
    result = "Adult"
else:
    result = "Minor"
# Ternary
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# 7. Truthy and Falsy Values: Python treats some values as True and others as False.
# Falsy Values: False, None, 0, 0.0, '', "", [], (), {}, set()
name = ""
if name:
    print("Name exists")
else:
    print("Empty name")
# Truthy Values: 1, -5, "Hello", [1, 2], (True)
items = [1, 2, 3]
if items:
    print("List is not empty")

# 8. match / case (Python 3.10+): Works like a switch statement in other languages.
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
# Multiple Cases
day = 6
match day:
    case 6 | 7:
        print("Weekend")
    case _:
        print("Weekday")

# Interview Questions
# Q1. Difference between if and elif?
# - if starts a condition check.
# - elif checks additional conditions if previous conditions are false.
# Q2. Difference between if and match?
# - if is used for complex conditions.
# - match is used for matching specific values.
# Q3. Can we write multiple elif blocks?: YES
# Q4. Can else exist without if?: NO

# Practice Programs
# Check Leap Year
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Check Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")