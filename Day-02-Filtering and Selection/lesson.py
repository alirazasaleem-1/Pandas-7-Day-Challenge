import pandas as pd 

df = pd.read_csv('students.csv')

print(df)

print(df['Name'])

print(df[['Name', 'Marks']])

print(df[df['Marks'] > 80])

print(
    df[
        (df['Marks'] > 80) &
        (df['City'] == 'Faisalabad')
    ]
)

print(
    df.sort_values(
        by="Marks",
        ascending=False
    )
)