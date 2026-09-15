#3. DATA CLEANING

#1 checking missing values or null values
print(df.isnull().all())
#2 check duplicates
print(df.duplicated().sum())
#3 drop duplicate values
df=df.drop_duplicates()
print(df)
#4 Convert date columns If dates are stored as strings
print(df[['Order Date','Ship Date']].dtypes)
df['Order Date']=pd.to_datetime(df['Order Date'],format='%d/%m/%Y')
df['Ship Date']=pd.to_datetime(df['Ship Date'],format='%d/%m/%Y')
print(df.dtypes)
