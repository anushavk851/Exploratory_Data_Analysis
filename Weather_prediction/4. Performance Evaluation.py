#Performance evaluation

#A. Confusion Matrix
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
cm=confusion_matrix(ytest,ypred)
print(cm)
print(df['weather'].unique())
labels=['drizzle','rain','sun','snow','fog']
cmd=ConfusionMatrixDisplay(cm,display_labels=labels)
cmd.plot()

#B. Accuracy score

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(ytest, ypred)
print("Accuracy:", accuracy)
