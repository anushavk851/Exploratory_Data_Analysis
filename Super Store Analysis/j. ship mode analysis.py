# 9. Ship Mode Analysis

#1 Number of orders/records for each Ship Mode
print("number of orders in each:",df['Ship Mode'].value_counts())

#2 Total Sales by Ship Mode
print("Total sales:",df.groupby('Ship Mode')['Sales'].sum())

#3 Average Sales by Ship Mode
print("average sales:",df.groupby('Ship Mode')['Sales'].mean())

#4 Most-used Ship Mode
a=df['Ship Mode'].value_counts().idxmax()
print("most used mode:",a)

#5 Ship Mode with highest Sales
a=df.groupby('Ship Mode')['Sales'].sum().idxmax()
print("highest sale:",a)

#6 Sort Ship Modes by Sales
a=df.groupby('Ship Mode')['Sales'].sum()
print("sorted:",a.sort_values())

#7 Create Ship Mode vs Sales bar chart
a=df.groupby('Ship Mode')['Sales'].sum()
sns.barplot(x=a.index,y=a.values,color='black')
plt.show()
