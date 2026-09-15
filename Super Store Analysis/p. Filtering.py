#Filtering 

#1 Sales greater than a chosen value
print("Sales > 10000:",df[df['Sales']>10000])
#2 Sales less than a chosen value
print("sales <100:",df[df['Sales']<100])
#3 Technology category
print("technology category",df[df['Category']=="Technology"])
#4 Furniture category
print("Furniture category",df[df['Category']=="Furniture"])
#5 Office Supplies category
print("Office Supplies category",df[df['Category']=="Office Supplies"])
#6 West region
print("west region",df[df['Region']=="West"])
#7 Consumer segment
print("consumer segment",df[df['Segment']=="Consumer"])
#8 Same-day/fast shipping mode
print("ship mode",df[df['Ship Mode']=="Same Day"])
#9 A particular state
print("state",df[df['State']=="Florida"])
#10 A particular city
print("city",df[df['City']=="Los Angeles"])
#11 A particular customer
print("customer",df[df['Customer ID']=="CG-12520"])
#12 Products with Sales above a chosen value
a=df.groupby('Product ID')['Sales'].sum()
print(a[a>1000])
