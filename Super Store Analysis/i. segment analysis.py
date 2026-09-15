# 8 SEGMENT ANALYSIS

#1 Number of records in each Segment
print("Number of records in each",df['Segment'].value_counts())

#2 Total Sales by Segment
print("total sales:",df.groupby('Segment')['Sales'].sum())

#3 Average Sales by Segment
print("average sales:",df.groupby('Segment')['Sales'].mean())

#4 Sort Segments by Sales by Highest-sales Segment
a=df.groupby('Segment')['Sales'].sum()
print("sorted from highest:",a.sort_values(ascending=False))

#5 Sort Segments by Sales by Lowest-sales Segment
a=df.groupby('Segment')['Sales'].sum()
print("sorted from lowest:",a.sort_values())

#6 Create Segment vs Sales bar chart
a=df.groupby('Segment')['Sales'].sum()
sns.barplot(x=a.index,y=a.values,color='red')
plt.show()
