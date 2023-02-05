import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("kc_house_data.csv")

x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, 2].values

y = y.reshape(len(y), 1)



from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc2 = StandardScaler()

x = sc.fit_transform(x)
y = sc2.fit_transform(y)



x_test, x_train, y_test, y_train = train_test_split(x, y, random_state=0, test_size=0.2)
# y_test = sc2.inverse_transform(y_test)
# print(y_test)

regressor = SVR(kernel="rbf")

regressor.fit(x_train, y_train)

y_pred = sc2.inverse_transform(regressor.predict(sc.fit_transform(x_test)).reshape(-1,1))




np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), sc2.inverse_transform(y_test).reshape(len(sc2.inverse_transform(y_test)), 1)), 1))
