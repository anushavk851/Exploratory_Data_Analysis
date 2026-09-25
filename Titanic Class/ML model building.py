#I/P O/P Separation
x=df.drop(['Survived','Name','PassengerId','Ticket'],axis=1)
y=df['Survived']
x

#LABEL ENCODING
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x['Sex'] = le.fit_transform(x['Sex'])
x['Embarked'] = le.fit_transform(x['Embarked'])
x

#TRAIN-TEST SPLITTING
from sklearn.model_selection import  train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=41)
print(xtrain.shape)
print(xtest.shape)

#DATA BALANCING
print(df['Survived'].value_counts())
from imblearn.over_sampling import SMOTE
sm=SMOTE()
xtrain1,ytrain1=sm.fit_resample(xtrain,ytrain)
print(ytrain1.value_counts())

#FEATURE SCALING
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(xtrain1)
xtrain1=scaler.transform(xtrain1)
print(xtrain1)
xtest=scaler.transform(xtest)
print(xtest)

#MODEL BUILDING-DECISION TREE
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
#model training
dt.fit(xtrain1,ytrain1)
#model testing
ypred=dt.predict(xtest)
ypred














