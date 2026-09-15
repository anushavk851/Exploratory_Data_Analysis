#2. COLUMN UNDERSTANDING

#1 Unique Ship Modes
print("unique ship modes:",df['Ship Mode'].unique())
#2 Unique Segments
print("unique segments:",df['Segment'].unique())
#3 Unique Countries
print("unique countries:",df['Country'].unique())
#4 Number of unique Cities
print("number of unique city:",df['City'].nunique())
#5 Number of unique States
print("number of unique states:",df['State'].nunique())
#6 Unique Regions
print("unique regions:",df["Region"].unique())
#7 Unique Categories
print("unique category:",df['Category'].unique())
#8 Unique Sub-Categories
print("unique sub-categories:",df['Sub-Category'].unique())
#9 Number of unique Customers
print("Number of unique customers:",df['Customer ID'].nunique())
#10 Number of unique Products
print("Number of unique products:",df['Product ID'].nunique())
