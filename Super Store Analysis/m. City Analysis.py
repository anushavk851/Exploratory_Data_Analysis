# City Analysis

#1 Number of unique Cities
print("number of unique cities:",df['City'].nunique())
#2 Total Sales by City
print("total sales:",df.groupby('City')['Sales'].sum())
#3 Top 10 Cities by Sales
a=df.groupby('City')['Sales'].sum()
print("Top 10 City",a.sort_values().tail(10))   #used tail because dataset is in ascending order
#4 Bottom 10 Cities by Sales
a=df.groupby('City')['Sales'].sum()
print("bottom 10 cities",a.sort_values().head(10))  
#5 City with highest Sales
a=df.groupby('City')['Sales'].sum()
print("highest sale:",a.idxmax())
#6 City with lowest Sales
a=df.groupby('City')['Sales'].sum()
print("lowest sale:",a.idxmin())
#7 Create Top 10 Cities vs Sales bar char
a=df.groupby('City')['Sales'].sum()
b=a.sort_values(ascending=False).head(10)
plt.bar(b.index,b.values)
plt.show()
