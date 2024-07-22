import pandas as pd
movies_df=pd.read_csv(r"C:\\Users\\az\Downloads\\IMDB-Movie-Data.csv",index_col="Title")
a=movies_df.head()
print(a)
b=movies_df.tail(2)
print(b)
print(movies_df.info())
print(movies_df.shape)
dup=movies_df.add(movies_df)
print(dup.shape)
print(movies_df.columns)
movies_df.rename(columns={'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue_millions'}, inplace=True)
movies_df.columns = [col.lower() for col in movies_df]
print(movies_df.columns)

