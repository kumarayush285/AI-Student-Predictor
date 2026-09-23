import pandas as pd

# Load dataset
df = pd.read_csv("data/placement_data.csv")

print("Original Shape:", df.shape)

# --------------------------------
# 1. Remove duplicate rows
# --------------------------------

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

df = df.drop_duplicates()

# --------------------------------
# 2. Missing values
# --------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# --------------------------------
# 3. Separate numerical columns
# --------------------------------

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

# Fill numerical missing values with median
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# --------------------------------
# 4. Separate categorical columns
# --------------------------------

categorical_columns = df.select_dtypes(include=["object"]).columns

# Fill categorical missing values with mode
for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# --------------------------------
# 5. Check again
# --------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned Shape:", df.shape)

# --------------------------------
# 6. Save cleaned dataset
# --------------------------------

output_path = "data/cleaned_placement_data.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_path)