#Performance Evaluation

#A. Confusion Matrix
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
cm=confusion_matrix(ytest,ypred)
print(cm)
cmd=ConfusionMatrixDisplay(cm)
cmd.plot()

#B. Accuracy score
from sklearn.metrics import accuracy_score
acc=accuracy_score(ytest,ypred)
acc

#C Recall score
from sklearn.metrics import recall_score
re=recall_score(ytest,ypred)
re

#D Precision score
from sklearn.metrics import precision_score
pre=precision_score(ytest,ypred)
pre

#E F1 score
from sklearn.metrics import f1_score
f1=f1_score(ytest,ypred)
f1
