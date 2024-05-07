# -*- coding: utf-8 -*-
"""LVADSUSR172_NIVEDITHA_linear

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yGOD-_1rOyIrxVcgcyRVXQuWEkSWruVa

LINEAR REGRESSION
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

expenses = pd.read_csv("/content/expenses.csv")
expenses

expenses.info()

expenses.isnull().sum()

expenses['bmi'] = expenses['bmi'].fillna(expenses['bmi'].mean())

expenses.isnull().sum()

import matplotlib.pyplot as plt
numerical_columns = expenses.columns

# Create a box plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(20, 6))
    sns.histplot(expenses[column])
    plt.title(f'Bar Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

"""OUTLIERS"""

q1 = np.percentile(expenses['bmi'],0.25)
q3 = np.percentile(expenses['bmi'],0.75)
print(q1,q3)
iqr = q3-q1
print(iqr)
ul = q3 * (1.5 + iqr)
ll = q1 * (1.5 - iqr)
print(ul,ll)
expenses = expenses[(expenses['bmi'] < ul)]
expenses = expenses[(expenses['bmi'] > ll)]

expenses

"""ENCODING"""

#Encoding
le = LabelEncoder()
expenses['sex'] = le.fit_transform(expenses['sex'])
expenses['smoker'] = le.fit_transform(expenses['smoker'])
expenses['region'] = le.fit_transform(expenses['region'])

sns.heatmap(expenses.corr(numeric_only = True), annot = True)

#Train Test Split
X = expenses.iloc[:,:-1]
Y = expenses.iloc[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

X_test

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

y_pred[:5]

# Evaluate the model
mse = mean_squared_error(Y_test, y_pred)
print("Mean Squared Error:", mse)

rmse = mean_squared_error(Y_test, y_pred,squared=False)
print("Root Mean Squared Error:", rmse)

# Coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

r2_s = r2_score(Y_test, y_pred)
print("R2 Score:", r2_s)