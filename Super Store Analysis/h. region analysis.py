# 7. REGION ANALYSIS

#1 Number of records in each Region
print("number of records in each region:",df['Region'].value_counts())

#2 Total Sales by Region
print("total sale:",df.groupby('Region')['Sales'].sum())

#3 Average Sales by Region
print("average sale:",df.groupby('Region')['Sales'].mean())

#4 Sort Regions by Sales Highest-sales Region
a=df.groupby('Region')['Sales'].sum()
print("highest-sales",a.sort_values(ascending=False))

#5 Sort Regions by Sales Lowest-sales Region
a=df.groupby('Region')['Sales'].sum()
print("lowest-sales",a.sort_values())

#6 Create Region vs Sales bar chart
a=df.groupby('Region')['Sales'].sum()
sns.barplot(x=a.index,y=a.values,color='brown')
plt.show()
