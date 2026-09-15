#6 SUB-CATEGORY ANALYSIS

#1 Total Sales for each Sub-Category
print("total sale in each sub category",df.groupby('Sub-Category')['Sales'].sum())

#2 Average Sales for each Sub-Category
print("average sales in each",df.groupby('Sub-Category')['Sales'].mean())

#3 Sort Sub-Categories by total Sales, highest → lowest
a=df.groupby('Sub-Category')['Sales'].sum()
print("sorted:",a.sort_values(ascending=False))

#4 Top 5 Sub-Categories by Sales
a=df.groupby('Sub-Category')['Sales'].sum()
print("Top 5",a.sort_values(ascending=False).head())

#5 Bottom 5 Sub-Categories by Sales
a=df.groupby('Sub-Category')['Sales'].sum()
print("bottom 5",a.sort_values().head())

#6 Highest-selling Sub-Category
a=df.groupby('Sub-Category')['Sales'].sum()
print("Highest",a.max())

#7 Lowest-selling Sub-Category
a=df.groupby('Sub-Category')['Sales'].sum()
print("lowest",a.min())

#8 Create Sub-Category vs Sales bar chart.
a = df.groupby('Sub-Category')['Sales'].sum()
sns.barplot(x=a.index,y=a.values,color='red')
plt.show()
