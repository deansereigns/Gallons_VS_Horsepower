# -*- coding: utf-8 -*-
"""Gallons Vs Horsepower.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHcGlCjjia2617Gf_BE8v9yfItGVYLwk
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dat = pd.read_csv('Horsepower Vs gallons per 100 miles.csv')
X = dat.iloc[:,:-1].values
y = dat.iloc[:,-1].values

print(X)

print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.4,random_state=0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,y_train)

y_pred = reg.predict(X_test)

plt.scatter(X_train,y_train,color='red')
plt.scatter(X_test,y_test,color ='blue')
plt.plot(X_test,y_pred,color = 'yellow')
plt.title('Gallons per 100 miles vs Horsepower/100')
plt.xlabel('Horsepower/100')
plt.ylabel('Gallons per 100 mies')
plt.scatter(0,reg.intercept_,color='green')
plt.scatter(3,reg.predict([[3]]),color ='Black')
plt.show()

