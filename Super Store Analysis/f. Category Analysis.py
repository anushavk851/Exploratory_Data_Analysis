# 5 CATEGORY ANALYSIS

#1 Number of category
print("Number of category:",df['Category'].nunique())

#2 category names
print("Category name:",df['Category'].unique())

#3 Number of sales record in each category
print("number of sales record:",df.groupby('Category')['Sales'].count())

#4 sum of total sales of each category
print("Sum of total sales:",df.groupby('Category')['Sales'].sum())

#5 average sales for each category
print("Average Sales:",df.groupby('Category')['Sales'].mean())

#6 the category with the highest total Sales
a=df.groupby('Category')['Sales'].sum()
print("Category with Highest total sales:",a.max())

#7 Find the category with the lowest total Sales
b=df.groupby('Category')['Sales'].sum()
print("lowest total sales:",b.min())

#8 Sort categories by total Sales Highest → lowest.
b=df.groupby('Category')['Sales'].sum()
print(b.sort_values(ascending=False))

#9 Category-Sales barchart
a=df.groupby('Category')['Sales'].sum()
plt.title("Category-Sales Analysis")
plt.bar(a.index,a,color='black')
plt.show()
