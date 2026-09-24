import pandas as pd
df=pd.read_csv('/content/financial-risk-for-Loan-approval.csv')
df

#DATA UNDERSTANDING

#1 first 3 rows
df.head(3)
#2 last 3 rows
df.tail(3)
#3 datatype
print(df.dtypes)
#4 shape
print(df.shape)
#5 dimension
print(df.ndim)
#6 size
print(df.size)
#7 describe
print(df.describe())
#8 columns
print(df.columns)
#9. Categorical columns
print(df.select_dtypes(include=object).columns)
#10. Numerical columns
print(df.select_dtypes(exclude=object).columns)
#11 Unique values
print(df.nunique())
#12 Target column value counts
print(df['LoanApproved'].value_counts())
