# -*- coding: utf-8 -*-
"""LR(3rd part).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10-3UNNTo_QwQ_S6_8nFWgLpnH-WTe8CP
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

data = pd.read_csv('/content/Metro-Interstate-Traffic-Volume-Encoded.csv')

data.head()

X = data.drop('traffic_volume',axis=1)
Y = data['traffic_volume']

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression

LR = LinearRegression()

LR.fit(xtrain,ytrain)

pred = LR.predict(xtest)

import sklearn.metrics as metrics



print('R Squared : ',metrics.r2_score(ytest,pred))

print('Mean Absolute Error : ',metrics.mean_absolute_error(ytest,pred))

print('Mean Squared Error : ',metrics.mean_squared_error(ytest,pred))

print('Root Mean Squared Error : ',np.sqrt(metrics.mean_squared_error(ytest,pred)))

"""Forward Selection
Lets proceed with the forward selection to get which feature is more important for the traffic_volume Prediction
In each iteration, we add one more feature and find the score till an addition of a new variable does not improve the performance of the model.

**Forward** **Selection**

Creating a GRID search to find the best single feature
"""

for i in range(len(data.columns)-1):
    X=  data[[data.columns[i]]]
    Y=  data[['traffic_volume']]
    xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.25,random_state = 0)
    LR.fit(xtrain,ytrain)
    pred = LR.predict(xtest)
    print(data.columns[i],': ',round(metrics.r2_score(ytest,pred),4))

for i in range(len(data.columns)-1):
    X=  data[['temp','Hour',data.columns[i]]]
    Y=  data[['traffic_volume']]
    xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.25,random_state = 0)
    LR.fit(xtrain,ytrain)
    pred = LR.predict(xtest)
    print(data.columns[i],round(metrics.r2_score(ytest,pred),4))

for i in range(len(data.columns)-1):
    X=  data[['temp','Hour','weather_description',data.columns[i]]]
    Y=  data[['traffic_volume']]
    xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.25,random_state = 0)
    LR.fit(xtrain,ytrain)
    pred = LR.predict(xtest)
    print(data.columns[i],round(metrics.r2_score(ytest,pred),4))

for i in range(len(data.columns)-1):
    X=  data[['temp','Hour','weather_description','holiday',data.columns[i]]]
    Y=  data[['traffic_volume']]
    xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size = 0.25,random_state = 0)
    LR.fit(xtrain,ytrain)
    pred = LR.predict(xtest)
    print(data.columns[i],round(metrics.r2_score(ytest,pred),4))

"""Polynomial Transformation:
To understand the need for polynomial regression, we will see the scatter plot of the residuals
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(15,8))
plt.scatter (ytest, pred) 
range = [ytest.min (), pred.max ()] 
plt.plot (range, range, 'red') 
plt.title('Predicted vs Actual ')
plt.xlabel ('Actual') 
plt.ylabel ('Predicted ') 
plt.show ()

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=2)

data1 = data.copy()

X = data1.drop('traffic_volume',axis=1)
Y= data1['traffic_volume']

"""Transforming the data"""

X = pf.fit_transform(X)

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.25,random_state=0)

LR = LinearRegression()

LR.fit(xtrain,ytrain)

pred = LR.predict(xtest)

print('R Squared : ',metrics.r2_score(ytest,pred))

print('Mean Absolute Error : ',metrics.mean_absolute_error(ytest,pred))

print('Mean Squared Error : ',metrics.mean_squared_error(ytest,pred))

print('Root Mean Squared Error : ',np.sqrt(metrics.mean_squared_error(ytest,pred)))

"""We can see now the R squared has increased and it is 65 percent which indicates that 65 percent of variation is reduced after transforming the data to polynomial regression"""

plt.figure(figsize=(15,8))
plt.scatter (ytest, pred) 
range = [ytest.min (), pred.max ()] 
plt.plot (range, range, 'red') 
plt.title('Polynomial Transformed Data')
plt.xlabel ('Actual') 
plt.ylabel ('predicted ') 
plt.show ()

"""we can see that still the line is not a best fit but it is more better than the original data. Transformed data has given a better performance thanthe original one"""