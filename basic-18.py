# 33. Database Programming (Python + SQL)
# - Database Programming allows Python applications to store, retrieve, update, and manage data using databases.

# Part 1: SQLite
# What is SQLite?
# Lightweight database
# Serverless (no separate database server required)
# Stores entire database in a single file
# Built into Python through sqlite3
# import sqlite3

# sqlite3 Module
# sqlite3 is Python's built-in module for working with SQLite databases.
# Features:
# Create databases
# Create tables
# Execute SQL queries
# Perform CRUD operations
# Handle transactions

# Connecting to Database
# Create/Open Database
import sqlite3

conn = sqlite3.connect("students.db")
print("Database connected")
# If database doesn't exist, it will be created automatically.

# Create Cursor
# Cursor executes SQL commands.
cursor = conn.cursor()

# Creating Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

conn.commit()

# CRUD Operations: CRUD = Create, Read, Update, Delete
# CREATE (Insert Data)
cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("Aman", 22)
)

conn.commit()

# READ (Fetch Data)
# Fetch All
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)
# Output: (1, 'Aman', 22)

# Fetch One
cursor.execute("SELECT * FROM students")

row = cursor.fetchone()

print(row)

# UPDATE
cursor.execute(
    "UPDATE students SET age=? WHERE name=?",
    (23, "Aman")
)

conn.commit()

# DELETE
cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("Aman",)
)

conn.commit()

# Closing Connection
conn.close()

# Transactions
# - A transaction ensures that all operations succeed together or fail together.
# Commit
conn.commit()
# Permanently saves changes.

# Rollback
try:
    cursor.execute("INSERT INTO students VALUES(1,'Aman',22)")
    conn.commit()

except:
    conn.rollback()
# If error occurs, all changes are undone.

# Prepared Statements
# - Prepared statements separate SQL code from data.
# Benefits:
# Faster execution
# Prevent SQL Injection
# Reusable
cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("Rahul", 25)
)

# Parameterized Queries
# Never do:
name = input()

query = f"SELECT * FROM students WHERE name='{name}'"
cursor.execute(query)
# ❌ SQL Injection Risk

# Use:
name = input()

cursor.execute(
    "SELECT * FROM students WHERE name=?",
    (name,)
)
# ✅ Safe

# Complete SQLite Example
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("Aman", 22)
)

conn.commit()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()

# Part 2: MySQL
# What is MySQL?
# Relational Database Management System (RDBMS)
# Server based
# Suitable for medium and large applications
# Popular package:
# pip install mysql-connector-python

# Connecting to MySQL
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="college"
)

cursor = conn.cursor()

# Insert Data
cursor.execute(
    "INSERT INTO students(name, age) VALUES(%s, %s)",
    ("Aman", 22)
)

conn.commit()
# Notice: %s
# is used instead of ?

# Read Data
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# Part 3: PostgreSQL
# What is PostgreSQL?
# Advanced open-source RDBMS
# ACID compliant
# Highly scalable
# Used in enterprise applications
# Install driver:
# pip install psycopg2

# Connect to PostgreSQL
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

# Insert Record
cursor.execute(
    "INSERT INTO students(name, age) VALUES(%s, %s)",
    ("Aman", 22)
)

conn.commit()

# Database Drivers
# - Drivers are libraries that allow Python to communicate with databases.

# Database - Driver
# SQLite - sqlite3
# MySQL - mysql-connector-python
# PostgreSQL - psycopg2
# SQL Server - pyodbc
# Oracle - cx_Oracle

# SQLAlchemy
# What is SQLAlchemy?
# A powerful Python database toolkit and ORM.
# Install:
# pip install sqlalchemy
# Benefits:
# Database-independent code
# ORM support
# Connection pooling
# Easier database operations

# SQLAlchemy Connection
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///students.db"
)

# Execute SQL
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT 1")
    )

    print(result.fetchone())

# ORM (Object Relational Mapping)
# - ORM maps database tables to Python classes.
# Without ORM:
# SELECT * FROM students
# With ORM:
# student.name

# ORM Example
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

# Table ↔ Python Class Mapping:
# students table
#        ↓
# Student class
#        ↓
# Student object

# Insert Using ORM
from sqlalchemy.orm import Session

with Session(engine) as session:

    s1 = Student(
        name="Aman",
        age=22
    )

    session.add(s1)
    session.commit()

# Query Using ORM
with Session(engine) as session:

    students = session.query(Student).all()

    for s in students:
        print(s.name, s.age)

# Connection Pooling
# - Connection Pool = Collection of reusable database connections.
# Benefits:
# Faster performance
# Less overhead
# Better scalability
engine = create_engine(
    "mysql+pymysql://user:pass@localhost/db",
    pool_size=10,
    max_overflow=20
)
# Flow
# Request
#    ↓
# Connection Pool
#    ↓
# Database
#    ↓
# Return Connection

# Database Migrations
# Migration = Version control for database schema.
# Used for:
# Creating tables
# Adding columns
# Removing columns
# Modifying schema

# Popular tool: pip install alembic

# Alembic Workflow
# Initialize: alembic init alembic
# Create migration: alembic revision -m "create students table"
# Apply migration: alembic upgrade head
# Rollback: alembic downgrade -1

# Interview Questions
# 1. Difference between SQLite and MySQL?
# SQLite - MySQL
# Serverless - Server Based
# Single File DB - Separate Server
# Lightweight - Scalable
# Local Apps - Production Apps

# 2. Why use parameterized queries?
# Prevent SQL Injection
# Safer
# Better performance

# 3. What is a transaction?
# - A group of database operations executed as a single unit.

# 4. What is ORM?
# ORM maps database tables to Python classes.

# 5. What is SQLAlchemy?
# - A Python database toolkit and ORM framework.

# 6. What is Connection Pooling?
# Reuse database connections rather than creating a new one every time.

# 7. What is Migration?
# - A controlled way to apply database schema changes over time.

# Learning Order
# SQLite
#  ↓
# sqlite3
#  ↓
# CRUD
#  ↓
# Transactions
#  ↓
# Parameterized Queries
#  ↓
# MySQL
#  ↓
# PostgreSQL
#  ↓
# Database Drivers
#  ↓
# SQLAlchemy
#  ↓
# ORM
#  ↓
# Connection Pooling
#  ↓
# Migrations (Alembic)