import pandas as pd 

df = pd.read_csv("practice.csv")

print("Total Students:", len(df))
print("Average Age:", df["Age"].mean())
print("Oldest Student Age:", df["Age"].max())
print("Youngest Student Age:", df["Age"].min())