#classification report
from sklearn.metrics import classification_report
report=classification_report(ytest,ypred)
print(report)
