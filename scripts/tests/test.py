#!/home/deploy/mlops_practice_4/venv/bin/python3

import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from catboost import CatBoostClassifier


df = pd.read_csv("/home/deploy/mlops_practice_4/data/raw/test.csv")
X = df.drop("outcome", axis = 1)
y = df['outcome']

def test():
   with open("/home/deploy/mlops_practice_4/data/model.pkl", "rb") as fd:
      clf = pickle.load(fd)
   y_pred = clf.predict(X)
   score = metrics.accuracy_score(y_pred, y) 
   assert score > 0.7