import pandas as pd
import numpy as np
import os


train_df = pd.read_csv('data/raw/train.csv', sep=',')
test_df = pd.read_csv('data/raw/test.csv', sep=',')
test_df['id'] = np.nan

def preprocessing(df):
  df.loc[df['capillary_refill_time'] == '3', 'capillary_refill_time'] = np.nan
  df.loc[(df['pain'] == 'slight') | (df['pain'] == 'moderate'), 'pain'] = 'mild_pain'
  df.loc[df['peristalsis'] == 'distend_small', 'peristalsis'] = np.nan
  df.loc[(df['abdominal_distention'] == 'none') | (df['abdominal_distention'] == 'None'), 'abdominal_distention'] = 'absent'
  df.loc[(df['nasogastric_tube'] == 'none') | (df['nasogastric_tube'] == 'None'), 'nasogastric_tube'] = 'absent'
  df.loc[(df['nasogastric_reflux'] == 'none') | (df['nasogastric_reflux'] == 'None'), 'nasogastric_reflux'] = 'absent'
  df.loc[df['nasogastric_reflux'] == 'slight', 'nasogastric_reflux'] = np.nan
  df.loc[df['rectal_exam_feces'] == 'None', 'rectal_exam_feces'] = 'absent'
  df.loc[df['rectal_exam_feces'] == 'serosanguious', 'rectal_exam_feces'] = np.nan
  df.loc[df['abdomen'] == 'None', 'abdomen'] = 'distend_small'
  df.loc[df['abdomo_appearance'] == 'None', 'abdomo_appearance'] = np.nan

  return df
  
def new_feature(df):
  df['protein'] = np.where((df['total_protein'] < 30), 'normal', 'many') # Разбиваем по количеству белка
  df["deviation_from_normal_temp"] = df["rectal_temp"].apply(lambda x: abs(x - 37.8))
  df['surgery_required'] = np.where((df['pain'] == 'extreme_pain') | (df['abdominal_distention'] == 'severe'), 'yes', 'no') # Добавим признак необходимости операции
  df['septicemia'] = np.where(df['mucous_membrane'] == 'bright_red', 'yes', 'no') # Добавим признак наличия септицемии
  df['intestinal_damage'] = np.where((df['abdomo_appearance'] == 2) |
                                     (df['abdomo_appearance'] == 3), 'yes', 'no') # Заменим признак Внешний вид живота (abdomo_appearance) на поражение кишечника
  df['nasogastric_reflux_ph'] = np.where((df['nasogastric_reflux_ph'] <= 2), 'normal', 'many') # nasogastric_reflux_ph
  df.drop(['id', 'lesion_2', 'lesion_3', 'rectal_temp'], axis= 1, inplace = True) # Убираем неликвидные признаки
  return df


def not_nan(df):
  # Заменим пропуски в категориальных данных предыдущими значением
  category_columns = list(df.select_dtypes(include=[object]).columns)
  for column in category_columns:
    df[column].fillna(method='ffill', inplace=True)
  # Заменим пропуски в числовых данных
  num_columns = list((df.select_dtypes(include=[int, float]).columns))
  for column in num_columns:
    df[column].fillna(df[column].mean(), inplace=True)
  return df
  

train_df = preprocessing(train_df)
test_df = preprocessing(test_df)
train_df = new_feature(train_df)
test_df = new_feature(test_df)
train_df = not_nan(train_df)
test_df = not_nan(test_df)

os.mkdir("data/features")

train_df.to_csv('data/features/train.csv', sep=',', index = False)
test_df.to_csv('data/features/test.csv', sep=',', index = False)

