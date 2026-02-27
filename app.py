import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("churn_dashboard_data.csv")

# Normaliza nomes das colunas
df.columns = df.columns.str.strip().str.replace(" ", "_")

st.title("📊 Customer Churn & Retention Strategy Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", df["Customer_ID"].nunique())
col2.metric("Total Monetary", round(df["Monetary"].sum(), 2))
col3.metric("High Risk (>0.8)", int((df["Churn_Probability"] > 0.8).sum()))

st.divider()

# Scatter
st.subheader("Customer Risk Map")

fig = px.scatter(
    df,
    x="Recency",
    y="Monetary",
    color="Churn_Probability",
    hover_data=["Customer_ID", "Frequency", "Action"]
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Action Distribution
st.subheader("Retention Actions")

action_counts = df["Action"].value_counts().reset_index()
action_counts.columns = ["Action", "Count"]

fig2 = px.bar(
    action_counts,
    x="Action",
    y="Count"
)

st.plotly_chart(fig2, use_container_width=True)
