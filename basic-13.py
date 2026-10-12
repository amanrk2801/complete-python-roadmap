# 22. Object-Oriented Programming (OOP) in Python
# - OOP (Object-Oriented Programming) is a programming paradigm that organizes code into objects and classes. It helps in creating reusable, maintainable, and scalable applications.

# 1. Classes & Objects
# Class - A class is a blueprint for creating objects.
class Car:
    pass

# Object - An object is an instance of a class.
class Car:
    pass
c1 = Car()
c2 = Car()
print(c1)
print(c2)

# Attributes - Attributes store data related to an object.
class Car:
    company = "Toyota"
c1 = Car()
print(c1.company)
# Output: Toyota

# Methods - Methods are functions defined inside a class.
class Car:
    def start(self):
        print("Car Started")
c1 = Car()
c1.start()
# Output : Car Started

# Constructor : A constructor initializes an object automatically when it is created.
class Student:
    def __init__(self):
        print("Constructor Called")
s1 = Student()
# Output : Constructor Called

# __init__ : Special method used as a constructor.
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aman")
print(s1.name) # Aman

# self -> self refers to the current object.
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
s1 = Student("Aman")
s1.display() # Aman

# 2. OOP Principles
# Encapsulation - Wrapping data and methods together.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
print(acc.get_balance()) # 1000

# Abstraction - Hiding implementation details from users.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
c = Car()
c.start()

# Inheritance - A child class acquires properties of a parent class.
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
d = Dog()
d.eat() # Eating
d.bark() # Barking

# Polymorphism - Same method name behaves differently.
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
for animal in [Dog(), Cat()]:
    animal.sound()
# Output:
# Bark
# Meow

# 3. Advanced OOP
# Class Variables: Shared by all objects.
class Student:
    school = "ABC School"
s1 = Student()
s2 = Student()
print(s1.school)
print(s2.school)

# Instance Variables: Unique for each object.
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aman")
s2 = Student("Rahul")
print(s1.name)
print(s2.name)

# Class Methods: Work with class-level data.
class Student:
    school = "ABC"
    @classmethod
    def change_school(cls, name):
        cls.school = name
Student.change_school("XYZ")
print(Student.school) # XYZ

# Static Methods: Independent utility methods.
class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(10, 5)) # 15

# @classmethod : Uses cls.
class Demo:
    @classmethod
    def show(cls):
        print("Class Method")
Demo.show()

# @staticmethod : Uses neither self nor cls.
class Demo:
    @staticmethod
    def show():
        print("Static Method")
Demo.show()

# Properties - Used to control attribute access.
class Person:
    def __init__(self):
        self.__age = 0
    @property
    def age(self):
        return self.__age
p = Person()
print(p.age)

# Getters and Setters
class Person:
    def __init__(self):
        self.__age = 0
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
p = Person()
p.age = 25
print(p.age) # 25

# Method Overriding - Child class overrides parent's method.
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound() # Bark

# Multiple Inheritance - A class can inherit from multiple parents.
class A:
    def show(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A, B):
    pass
c = C()
c.show()
c.display()

# MRO (Method Resolution Order) - Defines the order Python follows to search methods.
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
print(D.mro())
# Output:
# [<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>]

# super() - Calls parent class methods.
class Animal:
    def __init__(self):
        print("Animal Constructor")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
d = Dog()
# Output:
# Animal Constructor
# Dog Constructor

# Abstract Classes - Cannot be instantiated directly.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# Invalid: s = Shape()

# ABC (Abstract Base Class) - Provided by the abc module.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Interfaces Using Protocols - Python doesn't have traditional interfaces. We can use Protocol.
from typing import Protocol
class Drawable(Protocol):
    def draw(self):
        pass
class Circle:
    def draw(self):
        print("Drawing Circle")
def render(obj: Drawable):
    obj.draw()
c = Circle()
render(c)

# Output: Drawing Circle

# Interview Questions
# Q1. Difference between Class and Object?
# Class → Blueprint
# Object → Instance of a class

# Q2. What is self?
# self refers to the current object.

# Q3. Difference between Class Variable and Instance Variable?
# Class Variable   -> Shared by all objects
# Instance Variable -> Unique for every object

# Q4. Difference between @classmethod and @staticmethod?
# @classmethod  -> Uses cls
# @staticmethod -> Uses neither self nor cls

# Q5. What are the four pillars of OOP?
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# Q6. What is Method Overriding?
# - Redefining a parent class method in a child class.

# Q7. What is MRO?
# - Method Resolution Order determines which method Python executes first in inheritance hierarchies.

# Q8. Why use super()?
# - To access parent class methods and constructors.

# Q9. What is an Abstract Class?
# - A class containing one or more abstract methods that must be implemented by child classes.

# Q10. What is Polymorphism?
# - One interface, multiple implementations. Same method behaves differently for different objects.

# -------------------------------------------- #

# 23. Special / Dunder Methods in Python
# - Dunder (Double Underscore) Methods are special methods that start and end with __. Python automatically calls them to define how objects behave.
class Student:
    def __init__(self, name):
        self.name = name

# 1. __init__()
# - Constructor method. Runs automatically when an object is created.
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Aman")
print(s.name) # Aman

# 2. __str__()
# - Returns a user-friendly string representation.
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Student: {self.name}"
s = Student("Aman")
print(s) # Student: Aman

# 3. __repr__()
# - Returns an official/developer representation.
class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student('{self.name}')"
s = Student("Aman")
print(repr(s)) # Student('Aman')

# 4. __len__()
# - Defines behavior of len().
class MyList:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
obj = MyList([1, 2, 3, 4])
print(len(obj)) # 4

# 5. __eq__()
# - Defines == operator.
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __eq__(self, other):
        return self.marks == other.marks
s1 = Student(90)
s2 = Student(90)
print(s1 == s2) # True

# 6. __lt__()
# - Defines < operator.
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __lt__(self, other):
        return self.marks < other.marks
s1 = Student(80)
s2 = Student(90)
print(s1 < s2) # True

# 7. __gt__()
# - Defines > operator.
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __gt__(self, other):
        return self.marks > other.marks
s1 = Student(95)
s2 = Student(70)
print(s1 > s2) # True

# 8. __add__()
# - Defines + operator.
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return Number(self.value + other.value)
n1 = Number(10)
n2 = Number(20)
print((n1 + n2).value) # 30

# 9. __sub__()
# - Defines - operator.
class Number:
    def __init__(self, value):
        self.value = value
    def __sub__(self, other):
        return Number(self.value - other.value)
print((Number(20) - Number(5)).value) # 15

# 10. __mul__()
# - Defines * operator.
class Number:
    def __init__(self, value):
        self.value = value
    def __mul__(self, other):
        return Number(self.value * other.value)
print((Number(5) * Number(4)).value) # 20

# 11. __getitem__()
# - Enables indexing ([]).
class MyList:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        return self.items[index]
obj = MyList([10, 20, 30])
print(obj[1]) # 20

# 12. __setitem__()
# - Enables assignment with indexing.
class MyList:
    def __init__(self):
        self.items = [1, 2, 3]
    def __setitem__(self, index, value):
        self.items[index] = value
obj = MyList()
obj[0] = 100
print(obj.items) # [100, 2, 3]

# 13. __iter__()
# - Returns an iterator object.
class Numbers:
    def __init__(self):
        self.nums = [1, 2, 3]
    def __iter__(self):
        return iter(self.nums)
obj = Numbers()
for i in obj:
    print(i) # 1 2 3

# 14. __next__()
# - Returns next value in iteration.
class Counter:
    def __init__(self):
        self.count = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count <= 3:
            value = self.count
            self.count += 1
            return value
        raise StopIteration
obj = Counter()
for i in obj:
    print(i) # 1 2 3

# 15. __enter__() and __exit__()
# - Used in Context Managers (with statement).
class Demo:
    def __enter__(self):
        print("Resource Opened")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource Closed")
with Demo():
    print("Inside Block")
# Output
# Resource Opened
# Inside Block
# Resource Closed

# Operator Overloading
# - Changing the behavior of operators for custom objects.
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
b1 = Book(100)
b2 = Book(200)
print(b1 + b2) # 300

# Object Representation
# Using __str__()
class Car:
    def __str__(self):
        return "BMW Car"
print(Car()) # BMW Car

# Using __repr__()
class Car:
    def __repr__(self):
        return "Car()"
print(repr(Car())) # Car()

# Custom Containers
# - Create your own list-like container.
class MyContainer:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value

obj = MyContainer()
obj.data.append(10)
obj.data.append(20)
print(len(obj)) # 2
print(obj[0]) # 10

# Interview Summary
# Method -> Purpose
# __init__ -> Constructor
# __str__ -> User-friendly string
# __repr__ -> Developer representation
# __len__ -> Used by len()
# __eq__ -> ==
# __lt__ -> <
# __gt__ -> >
# __add__ -> +
# __sub__ -> -
# __mul__ -> *
# __getitem__ -> Indexing
# __setitem__ -> Assignment
# __iter__ -> Returns iterator
# __next__ -> Next element
# __enter__ -> Context manager start
# __exit__ -> Context manager end

# Remember: Dunder methods allow Python objects to behave like built-in types (list, string, dict, etc.), making custom classes more powerful and intuitive.