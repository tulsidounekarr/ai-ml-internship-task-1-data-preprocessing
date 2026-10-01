import pandas as pd
import matplotlib.pyplot as plt

# Load encoded dataset
df = pd.read_csv("titanic_encoded.csv")

# Numerical features where outliers are meaningful
numeric_columns = ["Age", "Fare"]
# -----------------------------
# Visualize outliers BEFORE removal
# -----------------------------
plt.figure(figsize=(12, 6))
df[numeric_columns].boxplot()
plt.title("Boxplots Before Outlier Removal")
plt.ylabel("Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("boxplots_before_outliers.png", dpi=300)
plt.show()

# -----------------------------
# Detect outliers using IQR
# -----------------------------
Q1 = df[numeric_columns].quantile(0.25)
Q3 = df[numeric_columns].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower bounds:")
print(lower_bound)

print("\nUpper bounds:")
print(upper_bound)

# Identify rows containing at least one outlier
outlier_mask = (
    (df[numeric_columns] < lower_bound)
    | (df[numeric_columns] > upper_bound)
).any(axis=1)

print("\nNumber of outlier rows:")
print(outlier_mask.sum())

print("\nOriginal dataset shape:")
print(df.shape)

# Remove outlier rows
df_clean = df[~outlier_mask].copy()

print("\nDataset shape after outlier removal:")
print(df_clean.shape)

# -----------------------------
# Visualize AFTER removal
# -----------------------------
plt.figure(figsize=(12, 6))
df_clean[numeric_columns].boxplot()
plt.title("Boxplots After Outlier Removal")
plt.ylabel("Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("boxplots_after_outliers.png", dpi=300)
plt.show()

# Save cleaned dataset
df_clean.to_csv("titanic_outlier_cleaned.csv", index=False)

print("\nOutlier-cleaned dataset saved as titanic_outlier_cleaned.csv")
print("Boxplots saved as:")
print("boxplots_before_outliers.png")
print("boxplots_after_outliers.png")