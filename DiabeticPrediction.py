import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import  LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("diabetes2.csv")

x = dataset.iloc[:, :-1].values

y = dataset.iloc[:, -1].values


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)


sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)


regressor = KNeighborsClassifier(n_neighbors=5)

regressor.fit(x_train, y_train)


y_pred = regressor.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))



accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print(matrix)
print(accuracy)


