import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 65, 90, 70, 85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nStatistics:")
print(df.describe())

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nEDA Completed Successfully!")