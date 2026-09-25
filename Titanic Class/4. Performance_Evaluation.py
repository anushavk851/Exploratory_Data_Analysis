#TRAINING AND TESTING PERFORMANCE

training_score=dt.score(xtrain1,ytrain1)
print("Training Score:",training_score)
testing_score=dt.score(xtest,ytest)
print("Testing Score:",testing_score)

#Performance evaluation

#A. Confusion Matrix
from sklearn.metrics import  confusion_matrix,ConfusionMatrixDisplay
cm=confusion_matrix(ytest,ypred)
print(cm)
cmd=ConfusionMatrixDisplay(cm)
cmd.plot()

#B. Accuracy score
from sklearn.metrics import accuracy_score
acc=accuracy_score(ytest,ypred)
acc

#C. RECALL
from sklearn.metrics import recall_score
recall=recall_score(ytest,ypred)
recall

#D. PRECISION SCORE
from sklearn.metrics import precision_score
pre=precision_score(ytest,ypred)
pre

#E. F1 Score
from sklearn.metrics import f1_score
score1=f1_score(ytest,ypred)
score1

