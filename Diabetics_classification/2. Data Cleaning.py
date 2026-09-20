#1 Null value check
print(df.isnull().sum()) #no null value

#2 duplicates
print(df.duplicated().sum())  #no duplicates
