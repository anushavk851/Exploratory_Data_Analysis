#DATA CLEANING

#1 checking missing values or null values
print(df.isnull().sum())

#2 check duplicates
print(df.duplicated().sum())

#3 drop duplicate values
df=df.drop_duplicates()
print(df)

#4 Convert date columns If dates are stored as strings
print(df[['Order Date','Ship Date']].dtypes)
df['Order Date']=pd.to_datetime(df['Order Date'],format='mixed')
df['Ship Date']=pd.to_datetime(df['Ship Date'],format='mixed')
print(df.dtypes)

#5 Shipping Date should be after Order Date.
df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
print(df[df['Shipping Duration'] < 0][['Order Date', 'Ship Date', 'Shipping Duration']])
# Remove invalid shipping durations
df = df[df['Shipping Duration'] >= 0]
print(df)
