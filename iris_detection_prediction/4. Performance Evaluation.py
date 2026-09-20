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
