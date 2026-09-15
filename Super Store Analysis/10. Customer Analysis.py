# 10. Customer Analysis

#1 Number of unique Customers
print("Number of unique customers:",df['Customer ID'].nunique())

#2 Total Sales for each Customer
print("Total Sales for each:",df.groupby('Customer ID')['Sales'].sum())

#3 Average Sales for each Customer
print("Average sales:",df.groupby('Customer ID')['Sales'].mean())

#4 Sort Customers by Sales
a=df.groupby('Customer ID')['Sales'].sum()
print("sorted:",a.sort_values())

#5 Top 10 Customers by Sales
a=df.groupby('Customer ID')['Sales'].sum()
print("Top 10:",a.sort_values(ascending=False).head(10))

#6 Bottom 10 Customers by Sales
a=df.groupby('Customer ID')['Sales'].sum()
print("bottom 10:",a.sort_values(ascending=False).tail(10))

#7 Customer with highest Sales
a=df.groupby('Customer ID')['Sales'].sum()
print("Customer with highest sale:",a.idxmax())

#8 Create Top 10 Customers vs Sales bar chart
a=df.groupby('Customer ID')['Sales'].sum()
b=a.sort_values(ascending=False).head(10)
sns.barplot(x=b.index,y=b.values)
plt.show()
