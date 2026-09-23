import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

plt.scatter(df["attendance"], df["cgpa"])

plt.xlabel("Attendance (%)")
plt.ylabel("CGPA")
plt.title("Attendance vs CGPA")

plt.show()

correlation = df["attendance"].corr(df["cgpa"])

print("Correlation between Attendance and CGPA:", correlation)