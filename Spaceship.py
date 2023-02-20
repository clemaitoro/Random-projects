import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier


dataset = pd.read_csv("train_space.csv")

dataset = dataset[["PassengerId", "Age", "VIP", "Destination","CryoSleep","HomePlanet", "RoomService",  "FoodCourt",  "ShoppingMall", "Cabin", "Name", "VRDeck", "Spa", "Transported"]]

x = dataset.iloc[:, :6].values
y = dataset.iloc[:, -1].values

dataset_test = pd.read_csv("test_space.csv")
dataset_test = dataset_test[["PassengerId", "Age", "VIP", "Destination","CryoSleep","HomePlanet", "RoomService",  "FoodCourt",  "ShoppingMall", "Cabin", "Name", "VRDeck", "Spa"]]
dataset_test[["Transported"]] = True

x_test = dataset_test.iloc[:, :6].values
y_test = dataset_test.iloc[:, -1].values


ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3,4,5])], remainder="passthrough")
x = np.array(ct.fit_transform(x))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x)
x = imputer.transform(x)
#
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3,4,5])], remainder="passthrough")
x_test = np.array(ct.fit_transform(x_test))
#
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x_test)
x_test = imputer.transform(x_test)

log = RandomForestClassifier(n_estimators=10)


log.fit(x, y)

y_pred = log.predict(x_test)


print(y_pred)
dataset_test["Transported"] = y_pred
# 
csv = dataset_test[['PassengerId', "Transported"]]
# 
csv.to_csv("submission2.csv", index=False)

