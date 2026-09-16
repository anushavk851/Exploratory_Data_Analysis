#Final Business Insights 

#A Which Category generates the most Sales?
a=df.groupby('Category')['Sales'].sum()
print("Highest selling category:",a.idxmax())

#B Which Sub-Category performs best?
a=df.groupby('Sub-Category')['Sales'].sum()
print("best Sub-Category:",a.idxmax())

#C Which Region generates the most Sales?
a=df.groupby('Region')['Sales'].sum()
print("Highest selling Region:",a.idxmax())

#D Which Segment generates the most Sales?
a=df.groupby('Segment')['Sales'].sum()
print("Highest selling Segment:",a.idxmax())

#E Which Ship Mode generates the most Sales?
a=df.groupby('Ship Mode')['Sales'].sum()
print("Highest selling Ship Mode:",a.idxmax())

#F Who is the top Customer?
a=df.groupby(['Customer ID','Customer Name'])['Sales'].sum()
print("Top Customer:",a.idxmax())


#G Which State has the highest Sales?
a=df.groupby('State')['Sales'].sum()
print("Highest selling State:",a.idxmax())

#H Which City has the highest Sales?
a=df.groupby('City')['Sales'].sum()
print("Highest selling city:",a.idxmax())

#I Which Product has the highest Sales?
a=df.groupby('Product Name')['Sales'].sum()
print("Highest selling product:",a.idxmax())

#J Which Year had the highest Sales?
df['Order Date']=pd.to_datetime(df['Order Date'],format="Mixed")
df['Year']=df['Order Date'].dt.year
a=df.groupby('Year')['Sales'].sum()
print("highest sale:",a.idxmax())

#K Which Month had the highest Sales?
df['Order Date']=pd.to_datetime(df['Order Date'],format="Mixed")
df['Month']=df['Order Date'].dt.month_name()
a=df.groupby('Month')['Sales'].sum()
print("highest sale:",a.idxmax())
