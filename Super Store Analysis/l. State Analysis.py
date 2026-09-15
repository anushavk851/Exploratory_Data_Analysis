# 11. State Analysis

#1 Number of unique States
print("number of unique states:",df['State'].nunique())

#2 Total Sales by State
print("total sales:",df.groupby('State')['Sales'].sum())

#3 Average Sales by State
print("Average sales:",df.groupby('State')['Sales'].mean())

#4 Top 10 States by Sales
a=df.groupby('State')['Sales'].sum()
print("Top 10 state",a.sort_values().tail(10))   #used tail because dataset is in ascending order

#5 Bottom 10 States by Sales
a=df.groupby('State')['Sales'].sum()
print("bottom 10 state",a.sort_values().head(10))   

#6 State with highest Sales
a=df.groupby('State')['Sales'].sum()
print("highest sale:",a.idxmax())

#7 State with lowest Sales
a=df.groupby('State')['Sales'].sum()
print("lowest sales:",a.idxmin())

#8 Create Top 10 States vs Sales bar chart
a=df.groupby('State')['Sales'].sum()
b=a.sort_values(ascending=False).head(10)
plt.bar(b.index,b.values)
plt.show()
