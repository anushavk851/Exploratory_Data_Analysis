#2 Data Cleaning

#1 null values handling
print(df.isnull().sum())
#2 duplicate values
print(df.duplicated().sum())
df=df.drop_duplicates()
#3 datatypes
print(df.dtypes)
