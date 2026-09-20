import pandas as pd
df=pd.read_csv('/content/seattle-weather_prediction.csv')
df

#Data understanding

#1 first 3 rows
print(df.head(3))
#2 last 3 rows
print(df.tail(3))
#3 Dimension
print("Dimension:",df.ndim)
#4 Total number of element
print("number of elemnt:",df.size)
#5 Datatype
print(df.dtypes)
#6 Shape
print(df.shape)
print("rows:",df.shape[0])
print("Columns:",df.shape[1])
#7 Column names
print("column names:",df.columns)
#8 statistical summary of numerical data
print(df.describe())
#9 complete info
print(df.info())
#10 unique values
print(df.nunique())
#11 unique outcomes
print(df['weather'].unique())
#12 value counts in each outcome.
print(df.value_counts('weather'))


