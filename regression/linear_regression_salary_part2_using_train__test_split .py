# -*- coding: utf-8 -*-
"""Linear_Regression_salary_part2_using_train__test_split.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFvXJNKi7GPMN8T20unP9bylXMhYOc0J
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('Salary.csv')
print(df.shape)
#df.head(5)

X = df.iloc[:,0:1]
y = df.iloc[:,1]

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.4, random_state=42)

regr = linear_model.LinearRegression()

regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

plt.scatter(X_test, y_test, c='blue') 
plt.plot(X_test, y_pred, color='g') 
plt.show()

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
mse=mse.astype(int)
mse

print(regr.predict([[3]]))