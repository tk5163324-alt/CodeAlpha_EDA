import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# IT EMPLOYEE PERFORMANCE & SALARY ANALYSIS
# ==========================================

# Load dataset
df = pd.read_csv("data/it_employee_data.csv")

# ------------------------------------------
# 1. Display first 5 records
# ------------------------------------------
print("\n===== FIRST 5 RECORDS =====")
print(df.head())

# ------------------------------------------
# 2. Dataset information
# ------------------------------------------
print("\n===== DATASET INFORMATION =====")
print(df.info())

# ------------------------------------------
# 3. Dataset shape
# ------------------------------------------
print("\n===== DATASET SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ------------------------------------------
# 4. Column names
# ------------------------------------------
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# ------------------------------------------
# 5. Statistical summary
# ------------------------------------------
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# ------------------------------------------
# 6. Missing values
# ------------------------------------------
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ------------------------------------------
# 7. Duplicate records
# ------------------------------------------
print("\n===== DUPLICATE RECORDS =====")
print("Number of duplicates:", df.duplicated().sum())

# ------------------------------------------
# 8. Average salary
# ------------------------------------------
print("\n===== AVERAGE SALARY =====")
print("Average Salary:", df["Salary"].mean())

# ------------------------------------------
# 9. Average performance
# ------------------------------------------
print("\n===== AVERAGE PERFORMANCE =====")
print("Average Performance Score:", df["Performance_Score"].mean())

# ------------------------------------------
# 10. Average salary by department
# ------------------------------------------
print("\n===== AVERAGE SALARY BY DEPARTMENT =====")
print(
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)

# ------------------------------------------
# 11. Average performance by department
# ------------------------------------------
print("\n===== AVERAGE PERFORMANCE BY DEPARTMENT =====")
print(
    df.groupby("Department")["Performance_Score"]
    .mean()
    .sort_values(ascending=False)
)

# ------------------------------------------
# 12. Most commonly used programming language
# ------------------------------------------
print("\n===== PROGRAMMING LANGUAGE USAGE =====")
print(df["Programming_Language"].value_counts())

# ------------------------------------------
# 13. Top 5 highest paid employees
# ------------------------------------------
print("\n===== TOP 5 HIGHEST PAID EMPLOYEES =====")
print(
    df.nlargest(5, "Salary")[
        ["Employee_ID", "Job_Role", "Experience_Years", "Salary"]
    ]
)

# ------------------------------------------
# 14. Top 5 performers
# ------------------------------------------
print("\n===== TOP 5 PERFORMERS =====")
print(
    df.nlargest(5, "Performance_Score")[
        ["Employee_ID", "Job_Role", "Performance_Score"]
    ]
)

# ------------------------------------------
# 15. Correlation analysis
# ------------------------------------------
print("\n===== CORRELATION ANALYSIS =====")

numeric_columns = [
    "Experience_Years",
    "Projects_Completed",
    "Training_Hours",
    "Performance_Score",
    "Salary",
    "Job_Satisfaction"
]

print(df[numeric_columns].corr())

print("\n===== ANALYSIS COMPLETED =====")

# ==========================================
# DATA VISUALIZATION
# ==========================================

import os

# Create output folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# 1. Average Salary by Department
plt.figure(figsize=(10, 6))

salary_by_dept = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)

salary_by_dept.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/average_salary_by_department.png")
plt.show()


# 2. Average Performance by Department
plt.figure(figsize=(10, 6))

performance_by_dept = (
    df.groupby("Department")["Performance_Score"]
    .mean()
    .sort_values(ascending=False)
)

performance_by_dept.plot(kind="bar")

plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/average_performance_by_department.png")
plt.show()


# 3. Experience vs Salary
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Experience_Years"],
    df["Salary"]
)

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.tight_layout()

plt.savefig("outputs/experience_vs_salary.png")
plt.show()


# 4. Training Hours vs Performance
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Training_Hours"],
    df["Performance_Score"]
)

plt.title("Training Hours vs Performance")
plt.xlabel("Training Hours")
plt.ylabel("Performance Score")
plt.tight_layout()

plt.savefig("outputs/training_vs_performance.png")
plt.show()


# 5. Programming Language Usage
plt.figure(figsize=(8, 6))

language_counts = df["Programming_Language"].value_counts()

language_counts.plot(kind="bar")

plt.title("Programming Language Usage")
plt.xlabel("Programming Language")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/programming_language_usage.png")
plt.show()


print("\n===== VISUALIZATIONS CREATED SUCCESSFULLY =====")
language_counts = df["Programming_Language"].value_counts()
# ============================================================
# KEY INSIGHTS
# ============================================================

dept_analysis = df.groupby("Department")[["Salary", "Performance_Score"]].mean()
print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

highest_salary_dept = dept_analysis["Salary"].idxmax()
highest_performance_dept = dept_analysis["Performance_Score"].idxmax()
most_used_language = language_counts.idxmax()

print(f"1. Highest average salary department: {highest_salary_dept}")
print(f"2. Highest average performance department: {highest_performance_dept}")
print(f"3. Most commonly used programming language: {most_used_language}")
print(f"4. Average employee salary: ₹{df['Salary'].mean():,.2f}")
print(f"5. Average performance score: {df['Performance_Score'].mean():.2f}")
print(f"6. Average experience: {df['Experience_Years'].mean():.2f} years")
print(f"7. Average projects completed: {df['Projects_Completed'].mean():.2f}")