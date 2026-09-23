import pandas as pd

df = pd.read_csv("data/students.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nBasic Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())



print("\nAverage CGPA:", df["cgpa"].mean())

print("Average Attendance:", df["attendance"].mean())

print("Highest CGPA:", df["cgpa"].max())

print("Lowest CGPA:", df["cgpa"].min())

print("Total Students:", len(df))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


print("\nInvalid CGPA:")
print(df[(df["cgpa"] < 0) | (df["cgpa"] > 10)])

print("\nInvalid Attendance:")
print(df[(df["attendance"] < 0) | (df["attendance"] > 100)])

print("\nInvalid Aptitude Score:")
print(df[(df["aptitude_score"] < 0) | (df["aptitude_score"] > 100)])

print("\nInvalid Projects:")
print(df[df["projects"] < 0])


X = df[
    [
        "cgpa",
        "attendance",
        "projects",
        "internship",
        "aptitude_score"
    ]
]

y = df["placement"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)


# ==============================
# DATA CLEANING CHECK
# ==============================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate rows
print("\n========== DUPLICATES ==========")
print("Duplicate rows:", df.duplicated().sum())

# Unique values
print("\n========== UNIQUE VALUES ==========")

for column in df.columns:
    print(column, ":", df[column].nunique())

# Categorical columns
print("\n========== CATEGORICAL COLUMNS ==========")

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print("\n", column)
    print(df[column].value_counts().head(10))
    