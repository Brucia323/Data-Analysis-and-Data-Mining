# load breast_cancer
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

breast_cancer = datasets.load_breast_cancer()
# split
x_train, x_test, y_train, y_test = train_test_split(
    breast_cancer.data, breast_cancer.target, test_size=0.2)
# svm
clf = svm.SVC(kernel='linear', C=100, gamma=0.001)
clf.fit(x_train, y_train)
# predict
y_pred = clf.predict(x_test)
# accuracy
acc = clf.score(x_test, y_test)
print(acc)
# draw
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_pred)
plt.show()
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
plt.show()
