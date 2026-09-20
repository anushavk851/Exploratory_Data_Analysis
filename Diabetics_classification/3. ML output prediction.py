#1 i/p and o/p separation
x=df.iloc[:,:8]
print(x.ndim)
print(x)
y=df['Outcome']
y

#2 train and test split
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=41)
print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)

#3 Feature Scaling
from sklearn.preprocessing import StandardScaler
Scaler=StandardScaler()
Scaler.fit(xtrain)    #collect and calculate std and mean
xtrain=Scaler.transform(xtrain)
print(xtrain)
xtest=Scaler.transform(xtest)
xtest

#4 KNN Model Building
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=7)
#model training
model.fit(xtrain,ytrain)
#model testing
ypred=model.predict(xtest)
ypred
