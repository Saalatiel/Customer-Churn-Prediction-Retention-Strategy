import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("online_retail.csv", encoding="ISO-8859-1")

st.title("📊 Customer Churn & Retention Strategy Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", df["Customer ID"].nunique())
col2.metric("Total Revenue", round((df["Quantity"] * df["Price"]).sum(), 2))
col3.metric("Total Transactions", df["Invoice"].nunique())

st.divider()

# Revenue by Country
st.subheader("Revenue by Country")

df["Revenue"] = df["Quantity"] * df["Price"]
country_rev = df.groupby("Country")["Revenue"].sum().reset_index()

fig = px.bar(
    country_rev.sort_values("Revenue", ascending=False).head(10),
    x="Country",
    y="Revenue",
    title="Top 10 Countries by Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Monthly Revenue Trend
st.subheader("Monthly Revenue Trend")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly_rev = df.groupby("YearMonth")["Revenue"].sum().reset_index()

fig2 = px.line(
    monthly_rev,
    x="YearMonth",
    y="Revenue",
    title="Revenue Over Time"
)

st.plotly_chart(fig2, use_container_width=True)
