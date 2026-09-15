# 17. Matplotlib Visualization

#1. Line Charts
#A. Sales by Year
# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')
# Extract Year
df['Year'] = df['Order Date'].dt.year
# Calculate total Sales by Year
a = df.groupby('Year')['Sales'].sum()
# Line chart
plt.plot(a.index, a.values, marker='o')
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

#B. Sales by Month
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Month']=df['Order Date'].dt.month
a=df.groupby('Month')['Sales'].sum()
plt.plot(a.index,a.values,marker="x")
plt.title("Sales by month")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#2 Histogram
#Distribution of Sales
plt.hist(df['Sales'])
plt.show()

#3 Pie Chart
#A Category percentage/share → pie chart
a=df['Category'].value_counts()
plt.pie(a.values,labels=a.index,autopct="%1.2f%%")
plt.show()

#B Segment percentage/share → pie chart
a=df['Segment'].value_counts()
plt.pie(a.values,labels=a.index,autopct="%1.2f%%")
plt.show()

