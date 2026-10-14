# 53. Data Science
# Data Science is the process of collecting, cleaning, analyzing, and visualizing data to extract useful insights. In Python, the most important libraries are:
# NumPy → Numerical computing
# Pandas → Data manipulation and analysis
# Matplotlib/Seaborn/Plotly → Data visualization

# 1. NumPy
# NumPy (Numerical Python) is used for fast mathematical and numerical operations.
# import numpy as np

# Arrays
# Arrays are NumPy's main data structure.
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(type(arr))
# Output:
# [10 20 30 40]
# <class 'numpy.ndarray'>

# 2D Array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)

# Vectorization
# - Perform operations on entire arrays without loops.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr * 2)
print(arr + 10)
# Output
# [2 4 6 8]
# [11 12 13 14]

# Instead of:
for i in arr:
    print(i * 2)
# Vectorized operations are much faster.

# Broadcasting
# - NumPy automatically expands smaller arrays.
import numpy as np

arr = np.array([1, 2, 3])

result = arr + 5

print(result)

# Output: [6 7 8]
# Example:
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix + 10)
# Output:
# [[11 12 13]
#  [14 15 16]]

# Indexing
# - Access elements using indexes.
arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[-1])
# Output:
# 10
# 40

# Slicing
print(arr[1:3])
# Output: [20 30]

# 2D Indexing
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[0, 1])
# Output: 2

# Linear Algebra
# Matrix Multiplication
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a @ b)

# Output:
# [[19 22]
#  [43 50]]

# Determinant
print(np.linalg.det(a))

# Inverse Matrix
print(np.linalg.inv(a))

# Eigenvalues
print(np.linalg.eig(a))

# 2. Pandas
# Pandas is used for data analysis and manipulation.
import pandas as pd

# Series
# One-dimensional labeled data.
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# DataFrame
# - A table with rows and columns.
data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [22, 25, 23]
}

df = pd.DataFrame(data)

print(df)
# Output:
#     Name  Age
# 0   Aman   22
# 1  Rahul   25
# 2  Priya   23

# Reading CSV
df = pd.read_csv("students.csv")

print(df.head())

# Reading Excel
df = pd.read_excel("students.xlsx")

print(df.head())

# Filtering
df = pd.DataFrame({
    "Name": ["Aman", "Rahul", "Priya"],
    "Marks": [90, 70, 85]
})

print(df[df["Marks"] > 80])
# Output:
#     Name  Marks
# 0   Aman     90
# 2  Priya     85

# GroupBy
# - Grouping data for aggregation.
data = {
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 42000]
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())
# Output
# Department
# HR    41000
# IT    55000

# Merge
# - Similar to SQL JOIN.
emp = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Aman", "Rahul", "Priya"]
})

salary = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [50000, 60000, 70000]
})

merged = pd.merge(emp, salary, on="ID")

print(merged)

# Join
df1 = pd.DataFrame({
    "Name": ["Aman", "Rahul"]
}, index=[1, 2])

df2 = pd.DataFrame({
    "Salary": [50000, 60000]
}, index=[1, 2])

print(df1.join(df2))

# Pivot Table
df = pd.DataFrame({
    "Month": ["Jan", "Jan", "Feb", "Feb"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 150, 120, 180]
})

pivot_table = df.pivot(
    index="Month",
    columns="Product",
    values="Sales"
)

print(pivot_table)

# Output
# Product    A    B
# Month
# Feb      120  180
# Jan      100  150

# Missing Data
df.isnull()
# Count missing values: df.isnull().sum()
# Fill missing values: df.fillna(0)
# Remove missing values: df.dropna()

# Data Cleaning
# Remove Duplicates
df.drop_duplicates()
# Rename Columns
df.rename(columns={"old": "new"})
# Change Data Type
df["Age"] = df["Age"].astype(int)

# 3. Data Visualization
# - Visualization helps understand data through charts.

# Matplotlib
# - Most commonly used plotting library.
import matplotlib.pyplot as plt

# Line Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)
plt.title("Line Chart")
plt.show()

# Bar Chart
names = ["A", "B", "C"]
sales = [100, 150, 80]

plt.bar(names, sales)
plt.show()

# Pie Chart
sizes = [30, 40, 30]

plt.pie(sizes, labels=["A", "B", "C"])
plt.show()

# Seaborn
# - Built on top of Matplotlib and provides better-looking charts.
import seaborn as sns

# Scatter Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.show()

# Histogram
sns.histplot(tips["total_bill"])
plt.show()

# Heatmap
corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

plt.show()

# Plotly
# - Interactive visualizations.
import plotly.express as px

# Interactive Scatter Plot
import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species"
)

fig.show()

# Interactive Line Chart
fig = px.line(
    x=[1, 2, 3, 4],
    y=[10, 20, 15, 30],
    title="Sales Trend"
)

fig.show()

# Interview Questions
# NumPy
# What is NumPy?
# Difference between list and NumPy array?
# What is broadcasting?
# What is vectorization?
# What is ndarray?

# Pandas
# Difference between Series and DataFrame?
# What is GroupBy?
# Difference between merge() and join()?
# How do you handle missing values?
# What is a pivot table?

# Visualization
# Difference between Matplotlib, Seaborn, and Plotly?
# When would you use a heatmap?
# Difference between line chart and scatter plot?
# Why use Plotly over Matplotlib?
# What is data visualization?

# Practice Task
import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya", "Aman"],
    "Department": ["IT", "HR", "IT", "IT"],
    "Salary": [50000, 40000, None, 50000]
}

df = pd.DataFrame(data)

# 1. Find missing values
# 2. Fill missing salary with average salary
# 3. Remove duplicates
# 4. Calculate average salary per department
# 5. Create bar chart of department salary

# -------------------------------------------- #
# 54. Machine Learning
# Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed.

# 1. ML Fundamentals