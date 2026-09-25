import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IT Employee Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD CUSTOM CSS
# ============================================================

css_file = Path("static/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/it_employee_data.csv")


df = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("📊 IT Employee Performance & Salary Analytics")

st.markdown(
    "### Exploratory Data Analysis Dashboard"
)

st.write(
    "Interactive analysis of employee salary, performance, "
    "experience, training, projects and programming languages."
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Filters")

departments = ["All"] + sorted(df["Department"].unique().tolist())

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)

languages = ["All"] + sorted(
    df["Programming_Language"].unique().tolist()
)

selected_language = st.sidebar.selectbox(
    "Select Programming Language",
    languages
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df.copy()

if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

if selected_language != "All":
    filtered_df = filtered_df[
        filtered_df["Programming_Language"] == selected_language
    ]


# ============================================================
# KPI CARDS
# ============================================================

total_employees = len(filtered_df)

average_salary = (
    filtered_df["Salary"].mean()
    if total_employees > 0
    else 0
)

average_performance = (
    filtered_df["Performance_Score"].mean()
    if total_employees > 0
    else 0
)

average_experience = (
    filtered_df["Experience_Years"].mean()
    if total_employees > 0
    else 0
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Employees",
        total_employees
    )

with col2:
    st.metric(
        "💰 Average Salary",
        f"₹{average_salary:,.0f}"
    )

with col3:
    st.metric(
        "⭐ Avg Performance",
        f"{average_performance:.2f}"
    )

with col4:
    st.metric(
        "💼 Avg Experience",
        f"{average_experience:.2f} years"
    )


st.divider()


# ============================================================
# NO DATA MESSAGE
# ============================================================

if filtered_df.empty:

    st.warning(
        "No employees match the selected filters."
    )

    st.stop()


# ============================================================
# SALARY BY DEPARTMENT
# ============================================================

salary_dept = (
    filtered_df
    .groupby("Department", as_index=False)["Salary"]
    .mean()
)

fig_salary = px.bar(
    salary_dept,
    x="Department",
    y="Salary",
    title="💰 Average Salary by Department",
)

fig_salary.update_layout(
    xaxis_title="Department",
    yaxis_title="Average Salary"
)

st.plotly_chart(
    fig_salary,
    use_container_width=True
)


# ============================================================
# PERFORMANCE BY DEPARTMENT
# ============================================================

performance_dept = (
    filtered_df
    .groupby("Department", as_index=False)["Performance_Score"]
    .mean()
)

fig_performance = px.bar(
    performance_dept,
    x="Department",
    y="Performance_Score",
    title="⭐ Average Performance by Department",
)

fig_performance.update_layout(
    xaxis_title="Department",
    yaxis_title="Performance Score"
)

st.plotly_chart(
    fig_performance,
    use_container_width=True
)


# ============================================================
# EXPERIENCE VS SALARY
# ============================================================

fig_experience = px.scatter(
    filtered_df,
    x="Experience_Years",
    y="Salary",
    size="Performance_Score",
    color="Department",
    hover_data=[
        "Employee_ID",
        "Job_Role",
        "Programming_Language"
    ],
    title="📈 Experience vs Salary"
)

st.plotly_chart(
    fig_experience,
    use_container_width=True
)


# ============================================================
# TRAINING VS PERFORMANCE
# ============================================================

fig_training = px.scatter(
    filtered_df,
    x="Training_Hours",
    y="Performance_Score",
    size="Projects_Completed",
    color="Department",
    hover_data=[
        "Employee_ID",
        "Job_Role"
    ],
    title="📚 Training Hours vs Performance"
)

st.plotly_chart(
    fig_training,
    use_container_width=True
)


# ============================================================
# PROGRAMMING LANGUAGE USAGE
# ============================================================

language_data = (
    filtered_df["Programming_Language"]
    .value_counts()
    .reset_index()
)

language_data.columns = [
    "Programming_Language",
    "Employee_Count"
]

fig_language = px.pie(
    language_data,
    names="Programming_Language",
    values="Employee_Count",
    title="💻 Programming Language Usage",
    hole=0.4
)

st.plotly_chart(
    fig_language,
    use_container_width=True
)


# ============================================================
# TOP PERFORMERS
# ============================================================

st.subheader("🏆 Top Performing Employees")

top_performers = (
    filtered_df
    .sort_values(
        "Performance_Score",
        ascending=False
    )
    .head(5)
)

st.dataframe(
    top_performers[
        [
            "Employee_ID",
            "Job_Role",
            "Department",
            "Performance_Score",
            "Salary"
        ]
    ],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DATA TABLE
# ============================================================

with st.expander("📋 View Complete Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "CodeAlpha Data Analytics Internship | "
    "IT Employee Performance & Salary Analysis"
)