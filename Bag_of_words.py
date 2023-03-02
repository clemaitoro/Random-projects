import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t", quoting=3)


# --------------------------- Cleaning the text ------------------------

import re
import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from gensim.utils import tokenize

corpus = []
for review in dataset["Review"]:
    review = re.sub("[^a-zA-Z]", " ", review).lower()
    tokens = list(tokenize(review))
    ps = SnowballStemmer("english")
    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    stemmed_tokens = [ps.stem(token) for token in tokens if not token in all_stopwords]
    stemmed_review = " ".join(stemmed_tokens)
    corpus.append(stemmed_review)


# ----------- Creating BoW model -------------------------------------

from gensim.models import Word2Vec
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

from gensim.test.utils import common_texts


model = Word2Vec(sentences=corpus, window=5, min_count=1, workers=4)

def get_doc_vector(doc):
    words = doc

    all_stopwords = stopwords.words("english")
    all_stopwords.remove("not")
    words = [word for word in words if not word in set(all_stopwords)]

    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if word_vectors:
        vector = np.mean(word_vectors, axis=0)
    else:
        vector = np.zeros(model.vector_size)

    return vector




X = [get_doc_vector(doc) for doc in corpus]

corpus = [doc.astype('float32') for doc in X]
corpus = [doc for doc in corpus if not np.isnan(np.sum(doc))]

max_length = max(len(doc) for doc in corpus)
X = pad_sequences(X, maxlen=max_length, padding="post", truncating="post", dtype="float32")
y = dataset.iloc[:, -1].values



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.svm import SVC

regressor = SVC(kernel="rbf", random_state=0)

regressor.fit(x_train, y_train)



y_pred = regressor.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))


from sklearn.metrics import accuracy_score,confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print(matrix)
print(accuracy)

