import pandas as pd
movies_df=pd.read_csv(r"C:\\Users\\az\Downloads\\IMDB-Movie-Data.csv",index_col="Title")
print(movies_df.head())
movies_df.tail(2)
movies_df.info()
movies_df.shape