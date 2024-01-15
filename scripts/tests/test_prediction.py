#!/home/deploy/mlops_practice_4/venv/bin/python3

import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from catboost import CatBoostClassifier


df = pd.read_csv('/home/deploy/mlops_practice_4/data/prepared/test.csv', sep=',')

X = df.drop("outcome", axis = 1)
y = df['outcome']


def predict():
   with open("/home/deploy/mlops_practice_4/data/model.pkl", "rb") as fd:
      clf = pickle.load(fd)
   y_pred = clf.predict(X)
   score = metrics.accuracy_score(y_pred, y)
   print(score)
   return score 


def test_prediction():
   predict()
   assert predict() > 0.7
