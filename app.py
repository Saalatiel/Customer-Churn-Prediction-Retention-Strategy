import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("churn_dashboard_data.csv", encoding="ISO-8859-1")

st.title("📊 Customer Churn & Retention Strategy Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", df["Customer ID"].nunique())
col2.metric("Total Monetary", round(df["Monetary"].sum(), 2))
col3.metric("High Risk Customers (>0.8)", int((df["Churn_Probability"] > 0.8).sum()))

st.divider()

# Customer Risk Map
st.subheader("Customer Risk Map (Recency vs Monetary)")

fig = px.scatter(
    df,
    x="Recency",
    y="Monetary",
    color="Churn_Probability",
    hover_data=["Customer ID", "Frequency", "Action"],
    title="Customer Risk Map",
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Action Distribution
st.subheader("Recommended Retention Actions")

action_counts = df["Action"].value_counts().reset_index()
action_counts.columns = ["Action", "Count"]

fig2 = px.bar(
    action_counts,
    x="Action",
    y="Count",
    title="Action Distribution",
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Top High Risk Customers Table
st.subheader("Top High Risk Customers")

top_risk = df.sort_values("Churn_Probability", ascending=False).head(20)
st.dataframe(top_risk[["Customer ID", "Recency", "Frequency", "Monetary", "Churn_Probability", "Action"]])
