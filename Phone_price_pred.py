import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv("train.csv")

x = dataset.iloc[:, :-1].values

y = dataset.iloc[:, -1].values

dataset_test = pd.read_csv("test.csv")
dataset_test["price_range"] = np.nan

x_test = dataset_test.iloc[:, 1:-1].values
y_test = dataset_test.iloc[:, -1].values


x_train, x_te, y_train, y_te = train_test_split(x, y, test_size=0.25)

clasifier = RandomForestClassifier(n_estimators=1000)

clasifier.fit(x, y)

y_pred = clasifier.predict(x_te)

print(confusion_matrix(y_te, y_pred))
print(accuracy_score(y_te, y_pred))

y_real_pred = clasifier.predict(x_test)
print(y_real_pred)