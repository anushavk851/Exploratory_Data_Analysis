import pandas as pd
df=pd.read_csv('/content/Thyroid_disease_prediction.csv')
df

#Data Understanding

#1. First 3 rows
print(df.head(3))
#2. last 3 rows
print(df.tail(3))
#3. Shape
print(df.shape)
#4. size
print(df.size)
#5. statistical summary
print(df.describe())
#6. column names
print(df.columns)
#7. data types
print(df.dtypes)
#8 dimension
print("Dimention:",df.ndim)
#9 unique values
print(df.nunique())
#10. Check Target
print(df['Recurred'].value_counts())
