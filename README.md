# 🎓 AI Student Placement Predictor

An AI/ML-based system that predicts whether an engineering student is likely to get placed based on academic performance, attendance, aptitude, projects, internships, and other career-readiness features.

## 📌 Project Overview

The **AI Student Placement Predictor** uses Machine Learning algorithms to analyze student data and predict placement outcomes.

The project includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Machine Learning Model Training
- Model Evaluation
- Feature Importance Analysis
- Student Placement Prediction

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Git & GitHub

## 📊 Dataset

The project uses a dataset containing **15,000 engineering student records** with multiple academic and career-readiness features.

The dataset contains information related to:

- CGPA
- Attendance
- Aptitude Score
- Projects
- Internships
- Technical Skills
- Career-readiness indicators
- Placement Status

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Missing value handling
2. Duplicate checking
3. Invalid value checking
4. Numerical feature processing
5. Categorical feature encoding
6. Feature scaling
7. Train-test splitting

## 📈 Exploratory Data Analysis

EDA was performed to understand relationships and patterns in the dataset.

Visualizations include:

- CGPA distribution
- Attendance analysis
- Placement distribution
- Feature relationships
- Average academic performance by placement status

## 🤖 Machine Learning Models

Three classification algorithms were implemented:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Decision Tree

A tree-based classification algorithm used to learn decision rules from student features.

### 3. Random Forest

An ensemble learning algorithm that combines multiple decision trees.

## 📊 Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC

The current evaluation showed Random Forest with approximately **79% accuracy** and **0.86 ROC-AUC** on the held-out test set.

> Note: These metrics are specific to the current dataset split and should not be interpreted as guaranteed real-world placement accuracy.

## 🎯 Prediction

The trained model can be used to predict the placement status of a new student based on their available academic and career-readiness information.

Example:

```text
Student Information
        ↓
Data Preprocessing
        ↓
Machine Learning Model
        ↓
Placement Prediction
        ↓
Placed / Not Placed
