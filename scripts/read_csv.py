import pandas as pd

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