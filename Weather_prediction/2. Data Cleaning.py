#Data Cleaning

#1 changing datatype from int to datetime
df['date']=pd.to_datetime(df['date'],format='mixed')
print(df.dtypes)
df['Month']=df['date'].dt.month
df['Dayofyear']=df['date'].dt.day_of_year
df['Year']=df['date'].dt.year
df=df.drop('date',axis=1)
print(df.columns)

#2 Null value check
print(df.isnull().sum()) #no null value

#3 duplicates
print(df.duplicated().sum())  #no duplicates
