import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC


dataset_train = pd.read_csv("train.csv")
dataset_test = pd.read_csv("test.csv")
dataset_test[["Survived"]] = 0


dataset_train_reorder = dataset_train[["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Name","Embarked","Ticket", "Cabin","Survived"]]

dataset_test_reorder = dataset_test[["PassengerId", "Pclass", "Sex",  "Age", "SibSp", "Parch", "Fare",  "Name","Embarked", "Ticket", "Cabin","Survived"]]



x = dataset_train_reorder.iloc[:, :-1].values
y = dataset_train_reorder.iloc[:, -1].values


ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [2])], remainder="passthrough")
x = np.array(ct.fit_transform(x))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, :8])
x[:, :8] = imputer.transform(x[:, :8])


x_test = dataset_test_reorder.iloc[:, :7].values
y_test = dataset_test_reorder.iloc[:, -1].values



ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [2])], remainder="passthrough")
x_test = np.array(ct.fit_transform(x_test))

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x_test[:, :8])
x_test[:, :8] = imputer.transform(x_test[:, :8])


regressor = SVC(random_state=0, kernel="linear")

regressor.fit(x[:, :8], y)

y_pred = regressor.predict(x_test[:, :8])
y_pred = y_pred.round(decimals=0)


print(y_pred)

# ---------------------------- Exporting data --------------------
dataset_test_reorder["Survived"] = y_pred

csv = dataset_test_reorder[['PassengerId',"Survived"]]

csv.to_csv("submission.csv", index=False)






