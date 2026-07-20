import pandas as pd

df = pd.read_csv("sales.csv")

summary = df.groupby("Department")["Sales"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print("Department Sales Report")
print(summary)