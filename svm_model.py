# -*- coding: utf-8 -*-
"""Final - SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pBy85lSug8WZoleN_0C-wLvP8auawMIm
"""

from sklearn import datasets
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

#Load the dataset
digits = datasets.load_digits()
X = digits.data
Y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.5, random_state = 0) #Tuning parameter

#Create the SVM model
model = SVC(kernel = 'linear', random_state = 0) #Tuning parameter
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Print out accuracy and confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

accuracies = cross_val_score(estimator = model, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))