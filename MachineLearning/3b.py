import pandas as pd

data = {
    'Name': ["Asha", "Ravi", "John",None],
    'Age': [20, 22, None, 25],
    'Gender': ["Female", "Male", "Male", "Male"],
    'Salary': [25000, 30000, 30000, 40000]
}
df = pd.DataFrame(data)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Name'].fillna("Unknown", inplace=True)
df.drop_duplicates(inplace=True)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
print(df)
