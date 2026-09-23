#3. Encoding 

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in df.columns:
  if i!='Age':
      df[i]=le.fit_transform(df[i])
df
