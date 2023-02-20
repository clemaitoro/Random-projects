import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("kc_house_data.csv")

x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, 2].values





x_test, x_train, y_test, y_train = train_test_split(x, y, random_state=0, test_size=0.2)

regressor = RandomForestRegressor(n_estimators=100)

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test).reshape(-1,1)

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

