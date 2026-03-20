import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\transaction\data\transactions.csv", encoding="utf-8")

                        # print(df.info())
                        # print(df.describe())
                        # print(df.columns)
                        # print(df.head())
#read all data
# print(df) 

#count missing value as column
print (df.isnull().sum())

# Drop rows with missing values
df_clean =df.dropna()


#lets fill null values
df['amount']=df["amount"].fillna(0)
df['customer_id'] = df['customer_id'].fillna(-1)

# now lets convert date column to proper datetime
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# filter rows
# only deposit
deposit = df[df['type']== 'deposit']

#transaction avove e 1000
big_txns = df[df['amount'] > 1000]


#now lets select column
#just transaction_id and amount
print(df[['transaction_id', 'amount']])


#now lets save the clean and filtered data back to csv

df_clean.to_csv("data\cleaned_transactions.csv", index=False)

# Total amount by transaction type
print(df.groupby('type')['amount'].sum())

# Number of transactions per customer
print(df.groupby('customer_id')['transaction_id'].count())

# Average transaction amount per type
print(df.groupby('type')['amount'].mean())


# Daily totals
print(df.groupby('date')['amount'].sum())

# Monthly totals
print(df.groupby(df['date'].dt.month)['amount'].sum())


# # Barc chart: total amount by type
# df.groupby('type')['amount'].sum().plot(kind='bar')
# plt.title("Total Amount by Transaction Type")
# plt.xlabel("Transaction Type")
# plt.ylabel("Amount")
# plt.show()

# # Line chart: daily totals
# df.groupby('date')['amount'].sum().plot(kind='line')
# plt.title("Daily Transaction Totals")
# plt.xlabel("Date")
# plt.ylabel("Amount")


df.groupby('type')['amount'].sum().to_csv("data/amount_by_type.csv")
