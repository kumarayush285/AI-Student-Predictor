import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# Load cleaned dataset
df = pd.read_csv("data/cleaned_placement_data.csv")

print("Dataset Shape:", df.shape)


# --------------------------------
# 1. Separate Target
# --------------------------------

target = "Placement_Status"

X = df.drop(columns=[target])
y = df[target]


# --------------------------------
# 2. Convert categorical columns
# --------------------------------

categorical_columns = X.select_dtypes(include=["object"]).columns

X = pd.get_dummies(
    X,
    columns=categorical_columns,
    drop_first=True
)


# --------------------------------
# 3. Convert target into numbers
# --------------------------------

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)


# --------------------------------
# 4. Train Random Forest
# --------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# --------------------------------
# 5. Feature Importance
# --------------------------------

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(
    ascending=False
)


print("\n========== TOP 15 IMPORTANT FEATURES ==========")

print(importance.head(15))


# --------------------------------
# 6. Plot Top 15 Features
# --------------------------------

plt.figure(figsize=(10, 7))

importance.head(15).sort_values().plot(
    kind="barh"
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Top 15 Feature Importance - Random Forest")

plt.tight_layout()
plt.show()