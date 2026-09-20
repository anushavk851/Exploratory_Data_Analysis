#classification report

from sklearn.metrics import classification_report
print("Classification Report:")
print(classification_report(ytest, ypred))
