import pandas as pd
import streamlit as st
import joblib

st.set_page_config(page_title="Employee Attrition Prediction")

st.title("📊 Employee Attrition Prediction")

model = joblib.load("employee_attrition_model.pkl")

st.header("Employee Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=50,
        value=10
    )

with col2:

    education = st.selectbox(
        "Education",
        [1,2,3,4,5]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        [1,2,3,4]
    )
    st.header("Job Information")

col1, col2 = st.columns(2)

with col1:

    gender_text = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

    gender = 1 if gender_text == "Male" else 0

    job_role = st.selectbox(
        "Job Role",
        [
            "Healthcare Representative",
            "Human Resources",
            "Laboratory Technician",
            "Manager",
            "Manufacturing Director",
            "Research Director",
            "Research Scientist",
            "Sales Executive",
            "Sales Representative"
        ]
    )

    job_level = st.selectbox(
        "Job Level",
        [1, 2, 3, 4, 5]
    )

    job_involvement = st.selectbox(
        "Job Involvement",
        [1, 2, 3, 4]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1, 2, 3, 4]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

with col2:

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=5000
    )

    monthly_rate = st.number_input(
        "Monthly Rate",
        min_value=1000,
        max_value=30000,
        value=10000
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=10,
        max_value=100,
        value=50
    )

    percent_salary_hike = st.number_input(
        "Percent Salary Hike",
        min_value=10,
        max_value=30,
        value=15
    )

    overtime_text = st.selectbox(
    "OverTime",
    ["Yes", "No"]
)

overtime = 1 if overtime_text == "Yes" else 0
            
        
    
st.header("Work Experience")

col1, col2 = st.columns(2)

with col1:

    num_companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        max_value=10,
        value=2
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=10
    )

    years_at_company = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=40,
        value=5
    )

    years_in_current_role = st.number_input(
        "Years in Current Role",
        min_value=0,
        max_value=20,
        value=3
    )

with col2:

    years_since_last_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        max_value=20,
        value=1
    )

    years_with_curr_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=20,
        value=3
    )

    training_times_last_year = st.selectbox(
        "Training Times Last Year",
        [0,1,2,3,4,5,6]
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [1,2,3,4]
    )
    st.header("Performance Details")

col1, col2 = st.columns(2)

with col1:

    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        max_value=2000,
        value=800
    )

    performance_rating = st.selectbox(
        "Performance Rating",
        [3,4]
    )

with col2:

    relationship_satisfaction = st.selectbox(
        "Relationship Satisfaction",
        [1,2,3,4]
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [0,1,2,3]
    )
    input_data = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [business_travel],
    "DailyRate": [daily_rate],
    "Department": [department],
    "DistanceFromHome": [distance_from_home],
    "Education": [education],
    "EducationField": [education_field],
    "EnvironmentSatisfaction": [environment_satisfaction],
    "Gender": [gender],
    "HourlyRate": [hourly_rate],
    "JobInvolvement": [job_involvement],
    "JobLevel": [job_level],
    "JobRole": [job_role],
    "JobSatisfaction": [job_satisfaction],
    "MaritalStatus": [marital_status],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [num_companies_worked],
    "OverTime": [overtime],
    "PercentSalaryHike": [percent_salary_hike],
    "PerformanceRating": [performance_rating],
    "RelationshipSatisfaction": [relationship_satisfaction],
    "StockOptionLevel": [stock_option_level],
    "TotalWorkingYears": [total_working_years],
    "TrainingTimesLastYear": [training_times_last_year],
    "WorkLifeBalance": [work_life_balance],
    "YearsAtCompany": [years_at_company],
    "YearsInCurrentRole": [years_in_current_role],
    "YearsSinceLastPromotion": [years_since_last_promotion],
    "YearsWithCurrManager": [years_with_curr_manager]
})
if st.button("🔮 Predict Attrition", use_container_width=True):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    stay_probability = probability[0][0] * 100
    leave_probability = probability[0][1] * 100

    confidence = max(stay_probability, leave_probability)

    st.divider()
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Employee is likely to leave the company.")
    else:
        st.success("✅ Employee is likely to stay with the company.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Stay Probability", f"{stay_probability:.2f}%")
        st.progress(stay_probability / 100)

    with col2:
        st.metric("Attrition Probability", f"{leave_probability:.2f}%")
        st.progress(leave_probability / 100)

    st.info(f"🎯 Model Confidence: {confidence:.2f}%")

st.set_page_config(page_title="Employee Attrition Prediction", layout="wide")
st.sidebar.title("📊 Employee Attrition Predictor")

st.sidebar.markdown("""
### About

This application predicts whether an employee is likely to leave the company using a Machine Learning model.

**Algorithm**
- Logistic Regression

**Built With**
- Python
- Scikit-learn
- Streamlit
- Pandas
""")
with st.expander("📋 View Input Summary"):
    st.dataframe(input_data)
    st.markdown("---")
st.markdown("---")

st.markdown("""
### 👨‍💻 Developer

**Y. Manjunath**

MBA - Data Analytics

Tools Used:
- Python
- Scikit-learn
- Pandas
- Streamlit
- Logistic Regression
""")
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)
from datetime import datetime

st.caption(f"Prediction Time: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
