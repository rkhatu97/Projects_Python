#!/usr/bin/env python
# coding: utf-8

import random
import json
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
import pickle

class Sentiment:
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"

class Review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()
        
    def get_sentiment(self):
        if self.score <= 2:
            return Sentiment.NEGATIVE
        elif self.score == 3:
            return Sentiment.NEUTRAL
        else: #Score of 4 or 5
            return Sentiment.POSITIVE

file_name = 'books.json'
reviews = []
with open(file_name) as f:
    for line in f:
        review = json.loads(line)
        reviews.append(Review(review['reviewText'], review['overall']))
        
reviews[4].sentiment

training, test = train_test_split(reviews, test_size=0.33, random_state=42)

print(training[1].text)


train_x = [x.text for x in training]
train_y = [x.sentiment for x in training]


test_x = [x.text for x in test]
test_y = [x.sentiment for x in test]

print(train_y.count(Sentiment.POSITIVE))
print(train_y.count(Sentiment.NEGATIVE))

vectorizer = TfidfVectorizer()
vectorizer.fit_transform(train_x)
train_x_vectors = vectorizer.fit_transform(train_x)
test_x_vectors = vectorizer.transform(test_x)

print(train_x[1])
print(train_x_vectors[1].toarray())

clf_svm = svm.SVC(kernel='linear')

clf_svm.fit(train_x_vectors, train_y)

test_x[0]

clf_svm.predict(test_x_vectors[0])


clf_dec = DecisionTreeClassifier()
clf_dec.fit(train_x_vectors, train_y)

clf_dec.predict(test_x_vectors[0])

clf_gnb = DecisionTreeClassifier()
clf_gnb.fit(train_x_vectors, train_y)

clf_gnb.predict(test_x_vectors[0])

clf_log = LogisticRegression()
clf_log.fit(train_x_vectors, train_y)

clf_log.predict(test_x_vectors[0])

#Mean Accuracy
print("Linear SVM:", round(clf_svm.score(test_x_vectors, test_y)*100, 2))
print("Decision Tree:", round(clf_dec.score(test_x_vectors, test_y)*100, 2))
print("GaussianNB:", round(clf_gnb.score(test_x_vectors, test_y)*100, 2))
print("Logistic Regression:", round(clf_log.score(test_x_vectors, test_y)*100, 2))


f1_score(test_y, clf_svm.predict(test_x_vectors), average=None, labels=[Sentiment.POSITIVE, Sentiment.NEGATIVE])

test_set = ['very fun', "bad book do not buy", 'horrible waste of time']
new_test = vectorizer.transform(test_set)

print(clf_svm.predict(new_test))

parameters = {'kernel': ('linear', 'rbf'), 'C': (1,4,8,16,32)}

svc = svm.SVC()
clf = GridSearchCV(svc, parameters, cv=5)
clf.fit(train_x_vectors, train_y)


print(clf.score(test_x_vectors, test_y))

with open('./sentiment_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('./vectorizer.pkl', 'wb') as v:
    pickle.dump(vectorizer, v)
    
with open('./sentiment_classifier.pkl', 'rb') as f:
    load_clf = pickle.load(f)

print(test_set[1])
print(load_clf.predict(new_test[1]))

