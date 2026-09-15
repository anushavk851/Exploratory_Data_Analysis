# Product Analysis

#1 Number of unique Products
print("number of unique products:",df['Product ID'].nunique())

#2 Total Sales by Product
print("total sales:",df.groupby('Product ID')['Sales'].sum())

#3 Average Sales by Product
print("average sales:",df.groupby('Product ID')['Sales'].mean())

#4 Sort Products by Sales
a=df.groupby('Product ID')['Sales'].sum()
print("sorted:",a.sort_values())

#5 Top 10 Products by Sales
a=df.groupby('Product ID')['Sales'].sum()
print("top 10:",a.sort_values().tail(10))

#6 Bottom 10 Products by Sales
a=df.groupby('Product ID')['Sales'].sum()
print("bottom 10:",a.sort_values().head(10))

#7 Product with highest Sales
a=df.groupby('Product ID')['Sales'].sum()
print("Highest:",a.idxmax())

#8 Product with lowest Sales
a=df.groupby('Product ID')['Sales'].sum()
print("lowest:",a.idxmin())

#9 Create Top 10 Products vs Sales bar chart
a=df.groupby('Product ID')['Sales'].sum()
b=a.sort_values().tail(10)
plt.bar(b.index,b.values)
plt.show()
