import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data
df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")

# Clean data
df['amount'] = df['amount'].fillna(0)
df['customer_id'] = df['customer_id'].fillna(-1)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# --- Streamlit UI ---
st.title("📊 Transaction Dashboard")

# Filters
customer_filter = st.selectbox("Select Customer ID", options=df['customer_id'].unique())
type_filter = st.multiselect("Select Transaction Types", options=df['type'].unique(), default=df['type'].unique())
date_range = st.date_input("Select Date Range", [df['date'].min(), df['date'].max()])

# Apply filters
filtered_df = df[
    (df['customer_id'] == customer_filter) &
    (df['type'].isin(type_filter)) &
    (df['date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])))
]

st.subheader("Filtered Transactions")
st.dataframe(filtered_df)

# --- Charts ---
st.subheader("Total Amount by Type")
amount_by_type = filtered_df.groupby('type')['amount'].sum()
st.bar_chart(amount_by_type)

st.subheader("Daily Totals")
daily_totals = filtered_df.groupby('date')['amount'].sum()
st.line_chart(daily_totals)

st.subheader("Top 5 Customers by Total Amount")
top_customers = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_customers)
