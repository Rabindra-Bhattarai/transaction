import streamlit as st
import pandas as pd

df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")
df['amount'] = df['amount'].fillna(0)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

st.title("📅 Time Trends")

daily_totals = df.groupby('date')['amount'].sum()
st.line_chart(daily_totals)
