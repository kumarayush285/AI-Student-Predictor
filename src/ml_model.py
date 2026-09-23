import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_auc_score
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/cleaned_placement_data.csv")

print("Dataset Shape:", df.shape)


# ==========================================
# 2. TARGET
# ==========================================

target = "Placement_Status"

X = df.drop(columns=[target])
y = df[target]


# ==========================================
# 3. REMOVE ID / LEAKAGE COLUMNS
# ==========================================

remove_columns = []

for column in X.columns:

    column_lower = column.lower()

    if (
        "student_id" in column_lower
        or "package" in column_lower
        or "salary" in column_lower
    ):
        remove_columns.append(column)

X = X.drop(columns=remove_columns)

print("\nRemoved Columns:")
print(remove_columns)


# ==========================================
# 4. IDENTIFY FEATURES
# ==========================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_features = X.select_dtypes(
    include=["object"]
).columns

print("\nNumeric Features:")
print(list(numeric_features))

print("\nCategorical Features:")
print(list(categorical_features))


# ==========================================
# 5. PREPROCESSING
# ==========================================

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])


# ==========================================
# 6. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ==========================================
# 7. MODELS
# ==========================================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=5000),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
}


# ==========================================
# 8. MODEL TRAINING + EVALUATION
# ==========================================

print("\n==========================================")
print("           MODEL COMPARISON")
print("==========================================")


for name, model in models.items():

    print("\nTraining:", name)

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    prediction = pipeline.predict(X_test)

    # --------------------------------------
# ROC-AUC
# --------------------------------------

probabilities = pipeline.predict_proba(X_test)

classes = list(pipeline.named_steps["model"].classes_)

positive_index = classes.index("Placed")

auc = roc_auc_score(
    y_test,
    probabilities[:, positive_index]
)

print(
    "ROC-AUC  :",
    round(auc, 4)
)


   