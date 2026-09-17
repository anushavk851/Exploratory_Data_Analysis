#KNN
#1 i/p and o/p separation
#i/p-x
x=df.iloc[:,:13]
print(x.ndim)
print(x
y=df['target']
print(y)

#2 train and test split
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=41)
print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)
print(xtrain)


#3 Featuring scaling
#standard scaler method
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(xtrain)
xtrain=scaler.transform(xtrain)
xtrain

xtest=scaler.transform(xtest)
xtest

#4 KNN Model Building
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=7)
#model training
model.fit(xtrain,ytrain)
#model testing
ypred=model.predict(xtest)
ypred










