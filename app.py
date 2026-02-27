import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("churn_dashboard_data.csv")

st.title("📊 Customer Churn & Retention Strategy Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", df["Customer_ID"].nunique())
col2.metric("Average Churn Probability", round(df["Churn_Probability"].mean(), 2))
col3.metric("High Risk Customers (>0.8)", len(df[df["Churn_Probability"] > 0.8]))

st.divider()

# Scatter Plot
st.subheader("Customer Risk Map")

fig = px.scatter(
    df,
    x="Recency",
    y="Monetary",
    color="Churn_Probability",
    color_continuous_scale="Viridis",
    title="Recency vs Monetary (Churn Risk)"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Action Distribution
st.subheader("Strategic Action Distribution")

action_counts = df["Action"].value_counts().reset_index()
action_counts.columns = ["Action", "Count"]

fig2 = px.bar(
    action_counts,
    x="Action",
    y="Count",
    color="Action",
    title="Recommended Retention Actions"
)

st.plotly_chart(fig2, use_container_width=True)
