import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

dataset_train = pd.read_csv("train.csv")
dataset_test = pd.read_csv("test.csv")
dataset_test[["Survived"]] = 0



dataset_train_reorder = dataset_train[["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Name","Ticket", "Cabin", "Embarked", "Survived"]]

dataset_test_reorder = dataset_test[["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare",  "Name", "Ticket", "Cabin", "Embarked", "Survived"]]







x = dataset_train_reorder.iloc[:, :-1].values
y = dataset_train_reorder.iloc[:, -1].values


ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [2])], remainder="passthrough")
x = np.array(ct.fit_transform(x))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, :8])
x[:, :8] = imputer.transform(x[:, :8])


x_test = dataset_test_reorder.iloc[:, :-1].values
y_test = dataset_test_reorder.iloc[:, -1].values

print(y_test)


ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [2])], remainder="passthrough")
x_test = np.array(ct.fit_transform(x_test))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, :8])
x_test[:, :8] = imputer.transform(x_test[:, :8])


regressor = LinearRegression()

regressor.fit(x[:, :8], y)

y_pred = regressor.predict(x_test[:, :8])
y_pred = y_pred.round(decimals=0)



print(y_pred.reshape(len(y_pred), 1))
print(y.reshape(len(y), 1))



