#1 i/p and o/p separation

x=df.drop('weather',axis=1)
print(x.ndim)
print(x)
y=df['weather']
y

#2. train and test split
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=41)
xtrain

#3. feature scaling
#standard scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(xtrain)
print(xtrain)

xtrain=scaler.transform(xtrain)
xtest=scaler.transform(xtest)
xtest

#4. KNN model building

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=7)
#model training
model.fit(xtrain,ytrain)
#model testing-prediction
ypred=model.predict(xtest)




print(ypred)
