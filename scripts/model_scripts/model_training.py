import pandas as pd
import numpy as np
import yaml
import os
import pickle
from catboost import CatBoostClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split


params = yaml.safe_load(open('./params.yaml'))["estimator"]

train_df = pd.read_csv('data/prepared/train.csv', sep=',')

X = train_df.drop("outcome", axis = 1)
y = train_df['outcome']

n_estimators = params["n_estimators"]

cbc = CatBoostClassifier(verbose=0, n_estimators=n_estimators)
cbc.fit(X, y)

with open("./data/model.pkl", "wb") as f:
    pickle.dump(cbc, f)
