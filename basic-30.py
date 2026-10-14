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
# What is Machine Learning?
# Instead of writing rules manually, we provide data and let the model learn the rules.

# Traditional Programming
# Input + Rules → Output

# Machine Learning
# Input + Output Data → ML Algorithm → Model

# Types of ML
# 1. Supervised Learning
# 2. Unsupervised Learning
# 3. Reinforcement Learning

# 2. Supervised Learning
# - In supervised learning, the dataset contains:
# Features (X) → Inputs
# Labels (Y) → Outputs
# - The model learns the relationship between X and Y.

# Examples
# Input - Output
# House Size - Price
# Email Text - Spam/Not Spam
# Student Marks - Pass/Fail

# Algorithms
# Linear Regression
# Logistic Regression
# Decision Trees
# Random Forest
# SVM
# KNN

# 3. Unsupervised Learning
# Data contains only inputs (X).
# No target/output column exists.
# Goal:
# - Find patterns
# - Group similar data
# - Reduce dimensions

# Examples
# Customer segmentation
# Product recommendations
# Market basket analysis

# Algorithms
# K-Means
# Hierarchical Clustering
# DBSCAN
# PCA

# 4. Regression
# - Used when output is a continuous value.
# Examples
# Predict:
# - House prices
# - Salary
# - Temperature
# - Stock values

# Simple Linear Regression
# Equation: y=mx+b
# Where:
# y = prediction
# x = feature
# m = slope
# b = intercept

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[5]]))

# Output: [10.]

# 5. Classification
# - Used when output belongs to categories.
# Examples
# - Spam / Not Spam
# - Pass / Fail
# - Disease / No Disease
# - Cat / Dog

# Types
# Binary Classification
# 0 or 1
# Yes or No

# Multi-class Classification
# Red
# Green
# Blue

# from sklearn.linear_model import LogisticRegression

# 6. Clustering
# - Grouping similar records together.

# Example
# Customer Data:
# Customer A → Young, Tech Lover
# Customer B → Similar Behavior
# ⇒ Same Cluster

# K-Means Clustering
# Steps:
# 1. Choose K clusters
# 2. Assign points
# 3. Calculate centroids
# 4. Repeat until stable
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(data)
# Applications:
# Market Segmentation
# Image Compression
# Recommendation Systems

# 7. Feature Engineering
# Feature engineering means creating better input features to improve model performance.
# Date Feature
# Original: 2026-10-14
# New Features:
# Year = 2026 Month = 10 Day = 14 Weekday = Tuesday
# Salary Data: Monthly Salary
# Create: Annual Salary

# Techniques
# - Feature Creation
# - Feature Selection
# - Feature Transformation
# - Encoding
# - Scaling

# 8. Train/Test Split
# Never train and test on the same data.
# Standard Split
# 80% Training
# 20% Testing
# or
# 70% Training
# 30% Testing

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Why?
# Training Data:
# - Learn patterns

# Testing Data:
# - Measure performance on unseen data

# 9. Cross-Validation
# Instead of using only one train-test split, divide data into multiple folds.

# 5-Fold Cross Validation
# Fold 1 → Test
# Fold 2-5 → Train
#
# Fold 2 → Test
# Fold 1,3,4,5 → Train
#
# ...

# Benefits:
# ✅ More reliable
# ✅ Uses data efficiently
# ✅ Reduces bias

from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print(scores)

# 10. Model Evaluation
# Regression Metrics
# MAE: Mean Absolute Error
from sklearn.metrics import mean_absolute_error

# MSE: Mean Squared Error
from sklearn.metrics import mean_squared_error

# RMSE
import numpy as np

rmse = np.sqrt(mse)

# R² Score
from sklearn.metrics import r2_score

# Classification Metrics
# Accuracy
from sklearn.metrics import accuracy_score
# Formula:
# Correct Predictions / Total Predictions

# Precision
# TP / (TP + FP)

# Recall
# TP / (TP + FN)

# F1 Score
# 2 × Precision × Recall
# -----------------------
# Precision + Recall

# Confusion Matrix
# -          | Pred Yes | Pred No
# Actual Yes | TP       | FN
# Actual No  | FP       | TN

from sklearn.metrics import confusion_matrix

# 11. Scikit-Learn
# - Most popular ML library in Python.
# Installation: pip install scikit-learn
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Advantages:
# - Easy API
# - Many algorithms
# - Data preprocessing
# - Evaluation tools
# - Hyperparameter tuning

# 12. Pipelines
# Pipeline combines multiple steps into one workflow.
# Without Pipeline:
# Scale Data
# ↓
# Train Model
# ↓
# Predict

# With Pipeline:
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)

# Benefits:
# ✅ Cleaner code
# ✅ Prevents data leakage
# ✅ Easy deployment

# 13. Hyperparameter Tuning
# - Hyperparameters are settings chosen before training.
RandomForest(
    n_estimators=100,
    max_depth=5
)

# Grid Search
# - Tries all combinations.
from sklearn.model_selection import GridSearchCV

params = {
    "max_depth": [3, 5, 7],
    "n_estimators": [50, 100]
}

grid = GridSearchCV(
    model,
    params,
    cv=5
)

grid.fit(X_train, y_train)

print(grid.best_params_)

# Random Search
# - Faster for large datasets.
from sklearn.model_selection import RandomizedSearchCV

# Complete ML Workflow
# Collect Data
#       ↓
# Clean Data
#       ↓
# Feature Engineering
#       ↓
# Train/Test Split
#       ↓
# Choose Model
#       ↓
# Train Model
#       ↓
# Cross Validation
#       ↓
# Evaluate Model
#       ↓
# Hyperparameter Tuning
#       ↓
# Deploy Model

# Interview Questions
# Q1: Difference between Supervised and Unsupervised Learning?
# - Supervised uses labeled data.
# - Unsupervised uses unlabeled data.

# Q2: What is Overfitting?
# Model memorizes training data and performs poorly on new data.

# Q3: Why use Cross Validation?
# Gives more reliable performance estimates.

# Q4: Difference between Regression and Classification?
# Regression predicts numerical values.
# Classification predicts categories/classes.

# Q5: What is Feature Engineering?
# Creating or transforming features to improve model performance.