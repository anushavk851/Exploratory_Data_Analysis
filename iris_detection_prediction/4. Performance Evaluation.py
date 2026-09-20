#Performance evaluation

#A confusion matrix
from sklearn.metrics import  confusion_matrix
cm=confusion_matrix(ytest,ypred)
print(cm)
#for displaying as heatmap
labels=['Iris-virginica','Iris-versicolor','Iris-setosa']
from sklearn.metrics import  ConfusionMatrixDisplay
cmd=ConfusionMatrixDisplay(cm,display_labels=labels)
cmd.plot()

#B Accuracy score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(ytest, ypred)
print("Accuracy:", accuracy)

#C. Recall score
from sklearn.metrics import recall_score
recall=recall_score(ytest,ypred,average="weighted")
recall

#D. Precision Score
from sklearn.metrics import precision_score
pre=precision_score(ytest,ypred,average="weighted")
pre

#E. F1 Score
from sklearn.metrics import f1_score
score=f1_score(ytest,ypred,average="weighted")
score
