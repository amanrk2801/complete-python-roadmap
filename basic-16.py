# 29. Date & Time in Python
# The datetime module is used to work with dates and times in Python.
# import datetime

# 1. datetime
# - Represents both date and time together.
from datetime import datetime

now = datetime.now()

print(now)
print(type(now))

# Output:
# 2026-10-13 10:30:45.123456
# <class 'datetime.datetime'>

# Access Components
from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 2. date : Represents only the date.
from datetime import date

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

# Create Custom Date
from datetime import date

d = date(2025, 12, 25)

print(d)

# 3. time: Represents only time.
from datetime import time

t = time(14, 30, 45)

print(t)
print(t.hour)
print(t.minute)
print(t.second)

# 4. timedelta: Used for date/time arithmetic.
from datetime import datetime, timedelta

today = datetime.now()

future = today + timedelta(days=7)

print(today)
print(future)

# Subtract Dates
from datetime import date

d1 = date(2026, 10, 13)
d2 = date(2026, 10, 1)

difference = d1 - d2

print(difference) # 12 days, 0:00:00
print(difference.days) # 12

# 5. Time Zones
# - A time zone represents a region's local time.
from datetime import datetime
from zoneinfo import ZoneInfo

india = datetime.now(ZoneInfo("Asia/Kolkata"))

print(india)

# 6. UTC (Coordinated Universal Time)
# - UTC is the global standard time.
from datetime import datetime, UTC

utc_time = datetime.now(UTC)

print(utc_time)

# Example:
from datetime import datetime, UTC

now = datetime.now(UTC)

print("UTC Time:", now)

# 7. Formatting: Convert datetime object to a string.
# strftime()
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted) # 13-10-2026 10:45:30

# Common Format Codes
# %Y  # Year (2026)
# %y  # Year (26)
#
# %m  # Month (01-12)
# %d  # Day (01-31)
#
# %H  # Hour (24-hour)
# %I  # Hour (12-hour)
#
# %M  # Minute
# %S  # Second
#
# %A  # Full weekday
# %B  # Full month name
#
# %p  # AM/PM

from datetime import datetime

now = datetime.now()

print(now.strftime("%A"))
print(now.strftime("%B"))

# 8. Parsing
# Convert string → datetime object.
# strptime()
from datetime import datetime

date_string = "13-10-2026"

dt = datetime.strptime(date_string, "%d-%m-%Y")

print(dt) # 2026-10-13 00:00:00

# Another Example
from datetime import datetime

text = "2026/10/13 15:30"

dt = datetime.strptime(text, "%Y/%m/%d %H:%M")

print(dt)

# 9. zoneinfo: Introduced in Python 3.9 for timezone support.
from zoneinfo import ZoneInfo
from datetime import datetime

india = datetime.now(ZoneInfo("Asia/Kolkata"))

usa = datetime.now(ZoneInfo("America/New_York"))

print("India:", india)
print("USA:", usa)

# Convert Between Time Zones
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))

india_time = utc_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)

print("UTC:", utc_time)
print("India:", india_time)

# Interview Questions
# 1. Difference between date, time, and datetime?
# date → Only date
# time → Only time
# datetime → Date + Time

# 2. What is timedelta used for?
# - To add or subtract days, hours, minutes, seconds from a date/time.

# 3. Difference between strftime() and strptime()?
# strftime()  # datetime → string
# strptime()  # string → datetime

# 4. Why use UTC?
# Standard worldwide time
# Avoid timezone confusion
# Common in servers and databases

# 5. What is zoneinfo?
# A built-in module for working with time zones in Python.

# Quick Revision
from datetime import datetime, date, time, timedelta, UTC
from zoneinfo import ZoneInfo

# Current datetime
datetime.now()

# Current date
date.today()

# Custom time
time(10, 30, 0)

# Add days
datetime.now() + timedelta(days=5)

# UTC time
datetime.now(UTC)

# Format
datetime.now().strftime("%d-%m-%Y")

# Parse
datetime.strptime("13-10-2026", "%d-%m-%Y")

# Timezone
datetime.now(ZoneInfo("Asia/Kolkata"))

# ✅ Key Functions to Remember: now(), today(), strftime(), strptime(), timedelta(), astimezone(), ZoneInfo()

# ---------------------------------------------- #
# 30. Math & Statistics in Python
# Python provides several built-in modules for mathematical calculations, statistics, random number generation, precise decimal arithmetic, and fraction operations.
# 1. math Module
# - The math module contains mathematical functions and constants.
import math

print(math.sqrt(25))      # 5.0
print(math.pow(2, 3))     # 8.0
print(math.factorial(5))  # 120
print(math.pi)            # 3.141592653589793

# Common Functions
import math

print(math.ceil(4.2))     # 5
print(math.floor(4.8))    # 4
print(math.fabs(-10))     # 10.0
print(math.gcd(12, 18))   # 6

# 2. statistics Module
# - Used for statistical calculations.
import statistics

nums = [10, 20, 30, 40, 50]

print(statistics.mean(nums))      # 30
print(statistics.median(nums))    # 30
print(statistics.mode(nums))      # 10

# Variance and Standard Deviation
import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]

print(statistics.variance(data)) # 4.571428571428571
print(statistics.stdev(data)) # 2.138089935299395

# 3. random Module
# - Used for generating random values.
# Random Float
import random
print(random.random()) # 0.736482
# Range: 0.0 <= value < 1.0
# Random Integer
import random
print(random.randint(1, 10)) # 7
# Range includes both ends.
# Random Choice
import random

colors = ["Red", "Blue", "Green"]

print(random.choice(colors))

# Shuffle
import random

nums = [1, 2, 3, 4, 5]

random.shuffle(nums)

print(nums)

# Random Sample
import random

numbers = [1, 2, 3, 4, 5, 6]

print(random.sample(numbers, 3)) # [6, 2, 4]

# 4. decimal Module
# - Used when high precision is required.

# Problem with Float
print(0.1 + 0.2) # 0.30000000000000004
# This happens because floating-point numbers are stored in binary.

# Using Decimal
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b) # 0.3

# Set Precision
from decimal import *

getcontext().prec = 5

print(Decimal("1") / Decimal("7")) # 0.14286

# 5. fractions Module
# - Used for exact fractional arithmetic.
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(1, 6)

print(f1 + f2) # 1/2

# Convert Decimal to Fraction
from fractions import Fraction

print(Fraction(0.5)) # 1/2

# Random Numbers
# Generate Lottery Number
import random

lottery = random.randint(100000, 999999)

print(lottery)

# Dice Simulation
import random

dice = random.randint(1, 6)

print(dice)

# Probability Basics
# Probability Formula:
# Probability = Favorable Outcomes / Total Outcomes
# Example: Coin Toss
favorable = 1
total = 2

probability = favorable / total

print(probability) # 0.5

# Example: Dice
# Probability of getting 6:
probability = 1 / 6

print(probability) # 0.16666666666666666

# Precision
# - Precision means how many digits are accurately represented.
# Float Precision
print(1/3) # 0.3333333333333333

# Decimal Precision
from decimal import *

getcontext().prec = 20

print(Decimal(1) / Decimal(3)) # 0.33333333333333333333

# Floating-Point Issues
# Comparison Problem
print(0.1 + 0.2 == 0.3) # False

# Correct Way
import math

print(math.isclose(0.1 + 0.2, 0.3)) # True

# Interview Questions
# Q1. Difference between random.randint() and random.random()?
random.randint(1, 10)  # Integer
random.random()        # Float between 0 and 1

# Q2. Why use Decimal instead of float?
# Higher precision
# Suitable for financial calculations
# Avoids floating-point errors

# Q3. What is the output?
from fractions import Fraction

print(Fraction(2, 4)) # 1/2
# (Fraction automatically simplifies)

# Practice Questions
# Easy
# - Find square root of a number.
# - Generate a random integer between 1 and 100.
# - Calculate mean of a list.
# - Add two fractions.
# - Show value of π.

# Medium
# - Simulate rolling a dice 100 times.
# - Find median of a list.
# - Generate 5 unique random numbers.
# - Calculate factorial of a number.
# - Compare float vs Decimal for 0.1 + 0.2.

# Advanced
# - Create a lottery number generator.
# - Build a coin toss simulator.
# - Calculate probability of drawing an Ace from a deck.
# - Create a fraction calculator.
# - Generate random passwords using random.

# ✅ Modules to Remember for Math & Statistics:
# import math
# import statistics
# import random
# from decimal import Decimal
# from fractions import Fraction
# These five modules cover most mathematical, statistical, randomization, precision, and fraction-related tasks in Python.

