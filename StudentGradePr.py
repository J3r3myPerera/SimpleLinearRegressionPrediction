# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T3mp8ASRzeBhZAe2qInH5WTPFHVAPMV1
"""



import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")

print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

print(data.head())

predict = "G3"

X = np.array (data.drop([predict], axis = 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

#To predict the data and when the accuracy is best under the thirty iterrations the model gets saved
best = 0
for _ in range (30):
  x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
  linear = linear_model.LinearRegression()
  linear.fit(x_train, y_train)
  acc = linear.score(x_test, y_test)
  print (acc)
  if acc > best:
    best = acc
    #To save the file using pickle
  with open("studentModel.pickle", "wb") as f:
    pickle.dump(linear, f)

pickle_in = open("studentModel.pickle", "rb")
linear = pickle.load(pickle_in)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
  print(predictions[x], x_test[x], y_test[x])

p = 'absences'
style.use("ggplot")
plt.scatter(data[p], data["G3"])
plt.xlabel(p)
plt.ylabel("Fina Grade")
plt.show()

