import pandas as pd 

df = pd.read_csv("employees.csv")

df["Age"] = df["Age"].fillna(0)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Age"].fillna("Unknown")

df = df.drop_duplicates()

df = df.rename(columns={
    "Department": "Dept"
})

print(df)