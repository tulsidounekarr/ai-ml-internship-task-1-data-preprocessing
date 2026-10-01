import pandas as pd

# Load the original dataset
df = pd.read_csv("titanic.csv")

print("Missing values BEFORE cleaning:")
print(df.isnull().sum())

# Fill Age using median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked using mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fill missing Cabin values with "Unknown"
df["Cabin"] = df["Cabin"].fillna("Unknown")

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved as titanic_cleaned.csv")