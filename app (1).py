
import streamlit as st
import pandas as pd

# Hospital Data
data = {
    "Patient_ID": ["P001","P002","P003","P004","P005",
                   "P006","P007","P008","P009","P010"],

    "Department": [
        "Cardiology","Neurology","Orthopedic","Cardiology","Pediatrics",
        "Neurology","Orthopedic","Pediatrics","Cardiology","Neurology"
    ],

    "Treatment": [
        "Surgery","Consultation","Surgery","Checkup","Treatment",
        "Surgery","Consultation","Treatment","Surgery","Checkup"
    ],

    "Revenue": [50000,8000,40000,5000,12000,35000,7000,15000,55000,6000],

    "Healthcare_Cost": [30000,3000,25000,2000,7000,22000,2500,8000,32000,2500]
}

df = pd.DataFrame(data)

# Page title
st.set_page_config(
    page_title="Hospital Revenue Dashboard",
    layout="wide"
)

st.title("🏥 Hospital Revenue & Healthcare Cost Dashboard")
st.write("Analysis of hospital revenue, healthcare costs and net revenue.")

# Department filter
department = st.selectbox(
    "Select Department",
    ["All"] + sorted(df["Department"].unique().tolist())
)

# Filter data
if department != "All":
    filtered_df = df[df["Department"] == department]
else:
    filtered_df = df

# KPIs
total_revenue = filtered_df["Revenue"].sum()
total_cost = filtered_df["Healthcare_Cost"].sum()
net_revenue = total_revenue - total_cost
total_patients = filtered_df["Patient_ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,}")
col2.metric("Healthcare Cost", f"₹{total_cost:,}")
col3.metric("Net Revenue", f"₹{net_revenue:,}")
col4.metric("Total Patients", total_patients)

# Department analysis
st.subheader("Revenue vs Healthcare Cost")

department_data = filtered_df.groupby("Department")[
    ["Revenue", "Healthcare_Cost"]
].sum()

st.bar_chart(department_data)

# Treatment analysis
st.subheader("Treatment-wise Revenue")

treatment_data = filtered_df.groupby("Treatment")["Revenue"].sum()

st.bar_chart(treatment_data)

# Data table
st.subheader("Hospital Data")

st.dataframe(filtered_df, use_container_width=True)
