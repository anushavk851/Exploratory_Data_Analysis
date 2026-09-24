#INPUT OUTPUT SEPARATION

x=df.drop('LoanApproved',axis=1)
print(x.ndim)
y=df['LoanApproved']
y
