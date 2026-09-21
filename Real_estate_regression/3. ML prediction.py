#1 I/p and O/p separation
x=df.iloc[:,1:7]
print(x.ndim)
print(x)
#o/p-y
y=df['Y house price of unit area']
print(y)

#2 train and test split
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=41)
print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)

#3 Featuring scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(xtrain)
xtrain=scaler.transform(xtrain)
print(xtrain)
xtest=scaler.transform(xtest)
print(xtest)

#4 KNN model building
from sklearn.neighbors import KNeighborsRegressor
model=KNeighborsRegressor(n_neighbors=7)
#model training
model.fit(xtrain,ytrain)
#model test
ypred=model.predict(xtest)
ypred

