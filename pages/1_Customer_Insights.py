import streamlit as st
import pandas as pd

df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")
df['amount'] = df['amount'].fillna(0)
df['customer_id'] = df['customer_id'].fillna(-1)

st.title("👥 Customer Insights")

top_customers = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)
