import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("kc_house_data.csv")

x = dataset.iloc[:, 3:-1]
y = dataset.iloc[:, 2]

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



regressor = PolynomialFeatures(degree=4)

x_poly = regressor.fit_transform(x)

x_test,x_train,y_test, y_train = train_test_split(x_poly, y, test_size=0.2, random_state=0)

poly_reg = LinearRegression()

poly_reg.fit(x_train, y_train)

y_pred = poly_reg.predict(x_test)

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))


