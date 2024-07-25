import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
print(movies_df.isnull())
print(movies_df.isnull().sum())
print(movies_df.dropna())
print(movies_df.dropna(axis=1))
revenue = movies_df['revenue_millions']
print(revenue.head())
revenue_mean = revenue.mean()
print(revenue_mean)
print(revenue.fillna(revenue_mean,inplace=True))
print(movies_df.isnull().sum())
print(movies_df.describe())
print(movies_df['genre'].describe())
print(movies_df['genre'].value_counts())
print(movies_df['genre'].value_counts().head(10))
genre_col = movies_df[['genre']]
print(type(genre_col))
subset = movies_df[['genre', 'rating']]
print(subset.head())

prom = movies_df.loc["Prometheus"]
print(prom)
prom = movies_df.iloc[1]
print(prom)
movie_subset = movies_df.loc['Prometheus':'Sing']
movie_subset = movies_df.iloc[1:4]
print(movie_subset)
condition = (movies_df['director'] == "Ridley Scott")
print(condition.head())
print(movies_df[movies_df['director'] == "Ridley Scott"])
print(movies_df[movies_df['rating'] >= 8.6].head(3))
print(movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'Ridley Scott')].head())
movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])].head()
print(movies_df[
    ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
    & (movies_df['rating'] > 8.0)
    & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))])

def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"
movies_df["rating_category"] = movies_df["rating"].apply(rating_function)
print(movies_df.head(2))
movies_df["rating_category"] = movies_df["rating"].apply(lambda x: 'good' if x >= 8.0 else 'bad')
print(movies_df.head(2))
print(plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}))
plt.scatter(x=movies_df['rating'],y=movies_df['revenue_millions'],color="red")
plt.show()

plt.hist(x=movies_df['rating'],bins=10)
plt.title("Rating")
plt.show()

plt.boxplot(x=movies_df['rating'])
plt.show()

sns.boxplot(x='rating_category', y='revenue_millions', data=movies_df)
plt.title("Boxplot of Revenue (in Millions) by Rating Category")
plt.show()

