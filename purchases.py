import pandas as pd
data={'apples':[3,2,0,1],'oranges':[0,3,7,2]}
purchases=pd.DataFrame(data)
print(purchases)
purchases=pd.DataFrame(data,index=['June','Robert','Lilly','David'])
print(purchases)
purchases.loc['June']
df=pd.read_csv(r"C:\Users\az\Downloads\purchases(1).csv")
print(df)