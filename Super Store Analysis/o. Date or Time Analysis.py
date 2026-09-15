#Date / Time Analysis

#1 Sales by Year
df['Order Date']=pd.to_datetime(df['Order Date'],format="Mixed")
df['Year']=df['Order Date'].dt.year
print("sales by year:",df.groupby('Year')['Sales'].sum())

#2 Highest-sales Year
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Year']=df['Order Date'].dt.year
a=df.groupby('Year')['Sales'].sum()
print("highest-sale year:",a.idxmax())

#3 Lowest-sales Year
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Year']=df['Order Date'].dt.year
a=df.groupby('Year')['Sales'].sum()
print("lowest-sale year:",a.idxmin())

#4 Year-wise Sales line chart
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Year']=df['Order Date'].dt.year
a=df.groupby('Year')['Sales'].sum()
sns.lineplot(x=a.index,y=a.values)
plt.show()

#5 Sales by Month
df['Order Date']=pd.to_datetime(df['Order Date'],format="Mixed")
df['Month']=df['Order Date'].dt.month
print("sales by month:",df.groupby('Month')['Sales'].sum())

#6 Highest-sales Month
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Month']=df['Order Date'].dt.month
a=df.groupby('Month')['Sales'].sum()
print("highest-sale month:",a.idxmax())

#7 Lowest-sales Month
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Month']=df['Order Date'].dt.month
a=df.groupby('Month')['Sales'].sum()
print("lowest-sale month:",a.idxmin())

#8 Monthly Sales line chart
df['Order Date']=pd.to_datetime(df['Order Date'],format="mixed")
df['Month']=df['Order Date'].dt.month
a=df.groupby('Month')['Sales'].sum()
sns.lineplot(x=a.index,y=a.values)
plt.show()

#9 Calculate shipping duration
df['Order Date'] = pd.to_datetime(df['Order Date'], format="mixed")
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format="mixed")
df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
print(df[['Order Date', 'Ship Date', 'Shipping Duration']])

#10 Find average shipping duration
print("Average shipping duration:", df['Shipping Duration'].mean())

#11 Find maximum shipping duration
print("Maximum shipping duration:", df['Shipping Duration'].max())

#12 Find minimum shipping duration
print("Minimum shipping duration:", df['Shipping Duration'].min())
#here the output is -314 which is impossible.so it mean some data have shipping date before order date.to handle this
print(df[df['Shipping Duration'] < 0][['Order Date', 'Ship Date', 'Shipping Duration']])
df = df[df['Shipping Duration'] >= 0]
print("Minimum shipping duration:", df['Shipping Duration'].min())
