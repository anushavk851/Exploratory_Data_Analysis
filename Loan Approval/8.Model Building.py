#MODEL BUILDING
from sklearn.naive_bayes import BernoulliNB
model=BernoulliNB()
#training model
model.fit(xtrain1,ytrain1)
#testing model
ypred=model.predict(xtest)
ypred
