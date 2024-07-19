import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,7,2]}
purchases=pd.DataFrame(data)
print(purchases)
purchases=pd.DataFrame(data,index=['June','Robert','Lilly','David'])
print(purchases)
purchases.loc['June']
df=pd.read_csv(r"C:\Users\az\Downloads\purchases(1).csv")
print(df)
df=pd.read_csv(r"C:\Users\az\Downloads\purchases(1).csv", index_col=0)
print(df)
df = pd.read_json(r"C:\Users\az\Downloads\purchases(1).json")
print(df)

import sqlite3
con=sqlite3.connect(r"C:\Users\az\Downloads\database.db")
df = pd.read_sql_query("SELECT * FROM purchases", con)
df.set_index('index',inplace=True)
print(df)
df.to_csv('new_purchases.csv')

df.to_json('new_purchases.json')

df.to_sql('new_purchases', con)

