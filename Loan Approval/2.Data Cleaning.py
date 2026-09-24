# DATA CLEANING

#1. NULL VALES
print(df.isnull().sum())
#2. Duplicate values
print(df.duplicated().sum())
#3 Date conversion
df['ApplicationDate'] = pd.to_datetime(df['ApplicationDate'])
df['Application Year'] = df['ApplicationDate'].dt.year
df['Application Month'] = df['ApplicationDate'].dt.month
df = df.drop('ApplicationDate', axis=1)
