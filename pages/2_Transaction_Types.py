import streamlit as st
import pandas as pd

df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")
df['amount'] = df['amount'].fillna(0)

st.title("💳 Transaction Types")

amount_by_type = df.groupby('type')['amount'].sum()
st.bar_chart(amount_by_type)
