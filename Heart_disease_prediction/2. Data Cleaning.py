#Data Cleaning
#1 null values handling
print(df.isnull().sum())
df['trestbps']=df['trestbps'].fillna(df['trestbps'].median())
df['restecg']=df['restecg'].fillna(df['restecg'].median())
df['thalach']=df['thalach'].fillna(df['thalach'].median())
df['oldpeak']=df['oldpeak'].fillna(df['oldpeak'].median())
df['slope']=df['slope'].fillna(df['slope'].median())
print(df.isnull().sum())
