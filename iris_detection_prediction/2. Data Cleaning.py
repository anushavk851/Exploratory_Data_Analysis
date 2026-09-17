#DATA CLEANING
#Dropping duplicate values
df=df.drop_duplicates()
df.duplicated().sum()
