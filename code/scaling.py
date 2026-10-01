import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the outlier-cleaned dataset
df = pd.read_csv("titanic_outlier_cleaned.csv")

# Numerical features to standardize
numeric_columns = ["Age", "Fare", "SibSp", "Parch", "Pclass"]

print("Before standardization:")
print(df[numeric_columns].head())

# Create scaler
scaler = StandardScaler()

# Standardize numerical features
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

print("\nAfter standardization:")
print(df[numeric_columns].head())

# Verify means are approximately 0
print("\nMeans after standardization:")
print(df[numeric_columns].mean())

# Save final preprocessed dataset
df.to_csv("titanic_preprocessed.csv", index=False)

print("\nFinal preprocessed dataset saved as titanic_preprocessed.csv")