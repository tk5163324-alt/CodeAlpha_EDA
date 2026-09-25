# 📊 IT Employee Performance & Salary Analysis

## CodeAlpha Data Analytics Internship — Task 2

An Exploratory Data Analysis (EDA) project that analyzes IT employee data to understand salary, performance, experience, training, projects, job satisfaction, and programming-language usage.

The project includes both a **Python-based EDA analysis** and an **interactive Streamlit dashboard**.

---

## 🎯 Project Objectives

- Analyze employee data using Python.
- Identify salary and performance patterns.
- Compare departments.
- Analyze experience and salary relationships.
- Study training hours and employee performance.
- Analyze programming-language usage.
- Identify top-performing and highest-paid employees.
- Create visualizations to communicate findings.
- Build an interactive analytics dashboard.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## 📁 Project Structure


CodeAlpha_EDA/
│
├── data/
│   └── it_employee_data.csv
│
├── outputs/
│   ├── average_salary_by_department.png
│   ├── average_performance_by_department.png
│   ├── experience_vs_salary.png
│   ├── training_vs_performance.png
│   └── programming_language_usage.png
│
├── static/
│   └── style.css
│
├── analysis.py
├── dashboard.py
├── requirements.txt
└── README.md


---

## 📊 Dataset

The dataset contains **30 IT employees** and **10 attributes**.


---

## 🔍 EDA Analysis

The project performs:

### 1. Dataset Inspection

- First five records
- Dataset information
- Number of rows and columns
- Column names

### 2. Data Quality Analysis

- Missing-value checking
- Duplicate-record checking

### 3. Statistical Analysis

Descriptive statistics are calculated for numerical variables such as:

- Experience
- Projects completed
- Training hours
- Performance
- Salary
- Job satisfaction

### 4. Department Analysis

Average salary and performance are calculated for each department.

### 5. Programming Language Analysis

The project analyzes the number of employees using each programming language.

### 6. Employee Analysis

The analysis identifies:

- Top 5 highest-paid employees
- Top 5 performers

### 7. Correlation Analysis

Relationships between numerical variables are analyzed using a correlation matrix.

---

## 📈 Visualizations

The project generates five visualizations:

1. Average Salary by Department
2. Average Performance by Department
3. Experience vs Salary
4. Training Hours vs Performance
5. Programming Language Usage

---

## 💡 Key Findings

Based on the current dataset:

- The average employee salary is approximately **₹73,133**.
- The average performance score is approximately **87.37**.
- The average employee experience is approximately **4.23 years**.
- The average number of completed projects is approximately **10.40**.
- **Python** is the most frequently used programming language in the dataset.
- Data Science has the highest average salary and average performance score among the departments represented in this dataset.
- The correlation analysis shows strong relationships among several numerical variables, including experience, projects completed, salary, performance, and job satisfaction.

> These findings describe the provided 30-employee dataset and should not be interpreted as representative of the entire IT industry.

---

## 🖥️ Interactive Dashboard

The project includes an interactive Streamlit dashboard.

The dashboard provides:

- Employee count
- Average salary
- Average performance
- Average experience
- Department filtering
- Programming-language filtering
- Interactive salary charts
- Interactive performance charts
- Experience vs salary analysis
- Training vs performance analysis
- Programming-language distribution
- Top-performing employee table
- Complete filtered dataset

---

## ▶️ How to Run the Project

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL


### 2. Open the project

cd CodeAlpha_EDA


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the EDA analysis

python analysis.py


### 5. Run the dashboard

python -m streamlit run dashboard.py


The Streamlit dashboard will open in your browser.

---

## 📌 Project Highlights

- Complete exploratory data analysis
- Data quality checking
- Statistical analysis
- Correlation analysis
- Multiple visualizations
- Interactive dashboard
- Department and programming-language filters
- GitHub-ready project structure

---

## 👩‍💻 Author

**Tannu Kumari**

CodeAlpha Data Analytics Internship