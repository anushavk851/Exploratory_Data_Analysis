#Data Understanding

#1 displaying first 5 rows
print(df.head())
#2 displaying last 4 rows
print(df.tail(4))
#3 shape
print("shape:",df.shape)
#4 number of rows
print("rows: ",df.shape[0])
#5 number of columns
print("columns:",df.shape[1])
#6 number of elements
print("Number of elements:",df.size)
#7 column names
print(df.columns)
#8 statistical summary of numerical data
print(df.describe())
#9 complete informations
df.info()
#10 dimension
print("Dimention:",df.ndim)
#11 datatype
print(df.dtypes)
#12 unique values
print(df.nunique())
#13 check null values
print(df.isnull().sum())
#14 to check value of outcome
print(df.value_counts('Outcome'))


