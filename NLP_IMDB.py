import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression


dataset = pd.read_csv("IMDB Dataset.csv")

nltk.download("stopwords")
nltk.download("punkt")



stemmer = SnowballStemmer("english")

corpus=[]

for i in range(50000):
    review = re.sub("[^a-zA-Z]", " ", dataset["sentiment"][i])
    review = review.lower()
    review = review.split()

    ss = SnowballStemmer("english")
    all_bad = stopwords.words("english")
    all_bad.remove("not")
    review = [ss.stem(word) for word in review if not word in set(all_bad)]
    review = "".join(review)

    corpus.append(review)



vectorizer = TfidfVectorizer()

x = dataset.iloc[:, 0]
y = dataset.iloc[:, -1]


le = LabelEncoder()
y = le.fit_transform(y)


x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.5)

x_train = vectorizer.fit_transform(x_train)

x_test = vectorizer.transform(x_test)


regressor  = LogisticRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))



accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print(matrix)
print(accuracy)



