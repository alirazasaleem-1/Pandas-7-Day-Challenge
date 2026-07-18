import pandas as pd 

ages = pd.Series([18, 20, 22])

print(ages)

data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [18, 20, 22]
}

df = pd.DataFrame(data)

print(df)

df = pd.read_csv("practice.csv")

print(df)
print(df.head())
print(df.shape) 
print(df.columns) 
print(df.info())