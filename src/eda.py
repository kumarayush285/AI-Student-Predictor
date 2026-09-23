import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned_placement_data.csv")

print("Dataset Shape:", df.shape)

# --------------------------------
# 1. Numerical Summary
# --------------------------------

print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe())

# --------------------------------
# 2. Histograms
# --------------------------------

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numeric_columns:
    plt.figure(figsize=(7, 5))

    plt.hist(df[column], bins=20)

    plt.xlabel(column)
    plt.ylabel("Number of Students")
    plt.title(f"Distribution of {column}")

    plt.show()


    # --------------------------------
# 3. Placement Distribution
# --------------------------------

print("\n========== PLACEMENT DISTRIBUTION ==========")

print(df["Placement_Status"].value_counts())

# Percentage
print("\nPlacement Percentage:")
print(df["Placement_Status"].value_counts(normalize=True) * 100)

# Bar chart
plt.figure(figsize=(7, 5))

df["Placement_Status"].value_counts().plot(kind="bar")

plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.title("Placement Distribution")

plt.show()


# --------------------------------
# 4. CGPA vs Placement
# --------------------------------

print("\n========== AVERAGE CGPA BY PLACEMENT ==========")

print(
    df.groupby("Placement_Status")["CGPA"].mean()
)

plt.figure(figsize=(7, 5))

df.groupby("Placement_Status")["CGPA"].mean().plot(
    kind="bar"
)

plt.xlabel("Placement Status")
plt.ylabel("Average CGPA")
plt.title("Average CGPA vs Placement")

plt.show()


# --------------------------------
# 5. Attendance vs Placement
# --------------------------------

print("\n========== AVERAGE ATTENDANCE BY PLACEMENT ==========")

print(
    df.groupby("Placement_Status")["Attendance_Percentage"].mean()
)

plt.figure(figsize=(7, 5))

df.groupby("Placement_Status")["Attendance_Percentage"].mean().plot(
    kind="bar"
)

plt.xlabel("Placement Status")
plt.ylabel("Average Attendance (%)")
plt.title("Average Attendance vs Placement")

plt.show()

# --------------------------------
# 6. Correlation Heatmap
# --------------------------------

print("\n========== CORRELATION MATRIX ==========")

# Select only numerical columns
numeric_df = df.select_dtypes(include=["int64", "float64"])

correlation_matrix = numeric_df.corr()

print(correlation_matrix)

# Plot heatmap
plt.figure(figsize=(14, 10))

plt.imshow(correlation_matrix, cmap="coolwarm")

plt.colorbar()

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()