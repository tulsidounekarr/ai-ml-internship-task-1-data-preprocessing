import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset shape
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display data types
print("\nData types:")
print(df.dtypes)

# Display missing values
print("\nMissing values:")
print(df.isnull().sum())

# Display basic dataset information
print("\nDataset information:")
df.info()