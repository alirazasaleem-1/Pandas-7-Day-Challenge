import pandas as pd 

df = pd.read_csv("sales.csv")

print(df)

# Group by Department
department_sales = df.groupby("Department")["Sales"].sum()

print(department_sales)

# Average Sales
average_sales = df.groupby("Department")["Sales"].mean()

print(average_sales)

# Count Records
sales_count = df.groupby("Department")["Sales"].count()

# Multiple Statistics
summary = df.groupby("Department")["Sales"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print(summary)

# Group by Multiple Columns
report = df.groupby(
    ["Department", "Product"]
)["Sales"].sum()

print(report)