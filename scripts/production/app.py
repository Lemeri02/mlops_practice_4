from flask import Flask, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from catboost import CatBoostClassifier


df = pd.read_csv("/home/deploy/mlops_practice_4/data/prepared/test.csv")
X = df.drop("outcome", axis = 1)
y = df['outcome']

app = Flask(__name__)


@app.route("/")
def hello():
	return ("Hello from Flask!")

@app.route("/predict")
def predict():
	with open("/home/deploy/mlops_practice_4/data/model.pkl", "rb") as fd:
		clf = pickle.load(fd)
	y_pred = clf.predict(X)
	return(jsonify({"score": metrics.accuracy_score(y_pred, y)}))

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=55555)