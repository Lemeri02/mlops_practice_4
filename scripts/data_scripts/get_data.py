#!/home/deploy/mlops_practice_4/venv/bin/python3

import pandas as pd


url_train = 'https://raw.githubusercontent.com/Lemeri02/mlops_practice_2_data/main/train.csv'
url_test = 'https://raw.githubusercontent.com/Lemeri02/mlops_practice_2_data/main/test.csv'
train_df = pd.read_csv(url_train)
test_df = pd.read_csv(url_test)


train_df.to_csv('/home/deploy/mlops_practice_4/data/raw/train.csv', sep=',', index = False)
test_df.to_csv('/home/deploy/mlops_practice_4/data/raw/test.csv', sep=',', index = False)