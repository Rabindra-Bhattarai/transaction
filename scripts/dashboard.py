import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Template

# Load data
df = pd.read_csv(r"D:/transaction/data/transactions.csv", encoding="utf-8")

# Clean data
df['amount'] = df['amount'].fillna(0)
df['customer_id'] = df['customer_id'].fillna(-1)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Analysis
missing = df.isnull().sum().to_frame("Missing Values")
amount_by_type = df.groupby('type')['amount'].sum()
top_customers = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).head(5)

# Charts
amount_by_type.plot(kind='bar', color='skyblue')
plt.title("Total Amount by Transaction Type")
plt.savefig("amount_by_type.png")
plt.close()

df.groupby('date')['amount'].sum().plot(kind='line', marker='o')
plt.title("Daily Transaction Totals")
plt.savefig("daily_totals.png")
plt.close()

top_customers.plot(kind='bar', color='orange')
plt.title("Top 5 Customers by Total Amount")
plt.savefig("top_customers.png")
plt.close()

# HTML Template
html_template = """
<html>
<head><title>Transaction Dashboard</title></head>
<body>
    <h1>Transaction Dashboard Report</h1>
    <h2>Missing Values</h2>
    {{ missing_html | safe }}
    <h2>Total Amount by Type</h2>
    {{ amount_html | safe }}
    <h2>Top 5 Customers</h2>
    {{ top_html | safe }}
    <h2>Charts</h2>
    <img src="amount_by_type.png" width="400">
    <img src="daily_totals.png" width="400">
    <img src="top_customers.png" width="400">
</body>
</html>
"""

template = Template(html_template)
html_out = template.render(
    missing_html=missing.to_html(),
    amount_html=amount_by_type.to_frame("Total Amount").to_html(),
    top_html=top_customers.to_frame("Total Amount").to_html()
)

with open("transaction_dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_out)

print("✅ Dashboard report generated: transaction_dashboard.html")
