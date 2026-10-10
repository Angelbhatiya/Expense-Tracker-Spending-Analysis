import pandas as pd

df=pd.read_csv("expenses.csv")
print(df)
print(df.head())

print(df.info())
print(df.describe())

print(df.isnull().sum())  #checking for null values
print("Duplicate rows:", df.duplicated().sum())  #checking for duplicate values

df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"])

total_expense = df["Amount"].sum()
print("Total Expense: ", total_expense)

avg_expense = df["Amount"].mean()
print("Average Expense: ", avg_expense)

highest_expense = df.loc[df["Amount"].idxmax()]
print("Highest Expense: ", highest_expense)

category_expense = df.groupby("Category")["Amount"].sum()
print(category_expense)

highest_category = category_expense.idxmax()
highest_category_amount = category_expense.max()
print("Highest spending Category :", highest_category)
print("Highest spending Category Amount :", highest_category_amount)

df["Month"] = df["Date"].dt.to_period("M")
monthly_expense = df.groupby("Month")["Amount"].sum()
print("Monthly-wise expense :", monthly_expense)

payment_mode = df.groupby("Payment_Mode")["Amount"].sum()
print("Payment Mode-wise expense :", payment_mode)

# Visualization

import matplotlib.pyplot as plt

#category-wise
category_expense.plot(kind="bar")
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

plt.show()

#Monthly expense graph
monthly_expense.plot(kind="line", marker="o")
plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.show()

# Seaborn Visualization

import seaborn as sns

sns.barplot(
    x=category_expense.index,
    y=category_expense.values
)
plt.title("Category-wise Expense")
plt.xticks(rotation=45)
plt.show()

