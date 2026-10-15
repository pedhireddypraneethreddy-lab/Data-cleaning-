import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Check again
print("\nAfter Cleaning:\n", df.isnull().sum())

# Display cleaned data
print("\nCleaned Dataset:\n", df.head())
