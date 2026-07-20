import pandas as pd 

df = pd.read_csv('employees.csv')

# print(df)

# Missing vaues
print(df.isnull())

# Count missing values
print(df.isnull().sum())

# Remove missing values
clean_df = df.dropna()

print(clean_df)

# Fill Missing Values
df['Age'] = df['Age'].fillna(0)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean()) # fill with average salary
df['Department'] = df['Department'].fillna("Unknown")

print(df)

# Remove Duplicates
df = df.drop_duplicates()
print(df)

# Rename Columns
df = df.rename(columns= {
    "Department" : "Dept"
})

print(df.columns)