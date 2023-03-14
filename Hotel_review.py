import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("Datafiniti_Hotel_Reviews.csv")




nltk.download("stopwords")

# print(dataset["reviews.text"])

corpus = []
for i in range(10000):
    review = re.sub("[^a-zA-Z]", " ", str(dataset["reviews.text"][i]))
    review = review.lower()
    review = review.split()

    stemmer = SnowballStemmer("english")
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    review = [stemmer.stem(word)for word in review if not word in set(all_stopwords)]
    review = "".join(review)

    corpus.append(review)


vectorizer = TfidfVectorizer()

x = dataset["reviews.text"]
y = dataset["reviews.rating"]

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.5)

threshold = 3.0

y_train = np.where(y_train > threshold, 'positive', 'negative')
y_test = np.where(y_test > threshold, 'positive', 'negative')

x_train = x_train.fillna('')
x_train = vectorizer.fit_transform(x_train)

x_test = x_test.fillna('')
x_test = vectorizer.transform(x_test)

regressor = LogisticRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print(accuracy_score(y_test, y_pred))


