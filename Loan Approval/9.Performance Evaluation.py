#PERFORMANCE EVALUATION

from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay,accuracy_score,recall_score,precision_score,f1_score

#A. Confusion matrix
cm=confusion_matrix(ytest,ypred)
print(cm)
cmd=ConfusionMatrixDisplay(cm)
cmd.plot()

#B. Accuracy score
acc=accuracy_score(ytest,ypred)
acc

#C. Recall score
recall=recall_score(ytest,ypred)
recall

#D. Precision score
pre=precision_score(ytest,ypred)
pre

#E. F1 score
f1=f1_score(ytest,ypred)
f1
