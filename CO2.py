import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset_train = pd.read_csv("BP-C02_EMMISSIONS_EUR.csv")

x_train = dataset_train.iloc[:, :-1].values
y_train = dataset_train.iloc[:, -1].values


dataset_pred = pd.read_excel("predictii.xlsx")
x_pred = dataset_pred.iloc[:, :-1].values
y_pred = dataset_pred.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_pred)

print(y_pred)

