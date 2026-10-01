import pandas as pd

# Load cleaned dataset
df = pd.read_csv("titanic_cleaned.csv")

print("Categorical columns before encoding:")
print(df[["Sex", "Embarked", "Cabin"]].dtypes)

# Create a simpler Deck feature from Cabin
df["Deck"] = df["Cabin"].apply(
    lambda x: x[0] if x != "Unknown" else "U"
)

# Drop original high-cardinality / text columns
df = df.drop(columns=["Cabin", "Name", "Ticket"])

# One-hot encode categorical features
df = pd.get_dummies(
    df,
    columns=["Sex", "Embarked", "Deck"],
    drop_first=True,
    dtype=int
)

print("\nDataset columns after encoding:")
print(df.columns.tolist())

print("\nData types after encoding:")
print(df.dtypes)

# Save encoded dataset
df.to_csv("titanic_encoded.csv", index=False)

print("\nEncoded dataset saved as titanic_encoded.csv")