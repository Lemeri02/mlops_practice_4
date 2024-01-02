import pandas as pd
import os
import pickle
import json
from catboost import CatBoostClassifier
from sklearn import metrics


cbc = pickle.load(open('./model.pkl', 'rb')) 

test_df = pd.read_csv('data/prepared/test.csv', sep=',')

X = test_df.drop("outcome", axis = 1)
y = test_df['outcome']

y_pred = cbc.predict(X)

score = metrics.accuracy_score(y, y_pred)

evaluate = {'score': score}

prc_file = os.path.join("evaluate", "score.json")
os.makedirs(os.path.join("evaluate"), exist_ok=True)

with open(prc_file, 'w') as f:
    json.dump(evaluate, f)
