import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")

# --- Cleaning ---
df['amount'] = df['amount'].fillna(0)
df['customer_id'] = df['customer_id'].fillna(-1)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# --- Summary ---
print("Missing values per column:")
print(df.isnull().sum())
print("\nTotal amount by type:")
print(df.groupby('type')['amount'].sum())
print("\nTransactions per customer:")
print(df.groupby('customer_id')['transaction_id'].count().head(10))
print("\nTop 5 customers by total amount:")
print(df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(5))

# --- Visualization ---
# 1. Total amount by transaction type
df.groupby('type')['amount'].sum().plot(kind='bar', color='skyblue')
plt.title("Total Amount by Transaction Type")
plt.xlabel("Type")
plt.ylabel("Amount")
plt.show()

# 2. Daily totals
df.groupby('date')['amount'].sum().plot(kind='line', marker='o')
plt.title("Daily Transaction Totals")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.show()

# 3. Top 5 customers by total amount
top_customers = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(5)
top_customers.plot(kind='bar', color='orange')
plt.title("Top 5 Customers by Total Amount")
plt.xlabel("Customer ID")
plt.ylabel("Total Amount")
plt.show()
