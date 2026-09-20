#Performance evaluation

#A confusion matrix
from sklearn.metrics import  confusion_matrix
cm=confusion_matrix(ytest,ypred)
print(cm)
from sklearn.metrics import  ConfusionMatrixDisplay
cmd=ConfusionMatrixDisplay(cm)
cmd.plot()

#B Accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(ytest, ypred)
print("Accuracy:", accuracy)

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

