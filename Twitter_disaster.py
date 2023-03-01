import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk

dataset_train = pd.read_csv("train.csv")
dataset_test = pd.read_csv("test.csv")
dataset_test = dataset_test[["id", "keyword", "location", "text"]]
dataset_test[["target"]] = 0


print(len(dataset_train["id"]))



from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download("stopwords")
nltk.download("punkt")

corpus_train = []

for i in range(7613):
    review_train = re.sub("[^a-zA-Z]", " ", dataset_train["text"][i])
    review_train = review_train.lower()
    review_train = review_train.split()

    ps = SnowballStemmer(language="english")
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    review_train = [ps.stem(word) for word in review_train if not word in set(all_stopwords)]
    review_train = " ".join(review_train)

    corpus_train.append(review_train)

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(dataset_train['text'])
y_train = dataset_train['target']
X_test = vectorizer.transform(dataset_test['text'])


corpus_test = []
for i in range(3263):
    review_test = re.sub("[^a-zA-Z]", " ", dataset_train["text"][i])
    review_test = review_test.lower()
    review_test = review_test.split()

    ps = SnowballStemmer(language="english")
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    review_test = [ps.stem(word) for word in review_test if not word in set(all_stopwords)]
    review_test = " ".join(review_test)

    corpus_test.append(review_test)



from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)


from sklearn.linear_model import LogisticRegression

regressor = LogisticRegression()

regressor.fit(X_train, y_train)



y_pred = regressor.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1))))

dataset_test["target"] = y_pred
csv = dataset_test[['id', "target"]]

csv.to_csv("submission2.csv", index=False)



