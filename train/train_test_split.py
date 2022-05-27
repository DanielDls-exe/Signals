import pandas as pd
from sklearn.model_selection import train_test_split
import os

separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

def generated_tts():
    df = pd.read_csv(f'{dir}/dataset.csv')
    df.columns = [i for i in range(df.shape[1])]
    df = df.rename(columns={63: 'Output'})
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]
    return train_test_split(X, Y, test_size=0.2)

def path_act():
    separator = os.path.sep
    path_act = os.path.dirname(os.path.abspath(__file__))
    dir = separator.join(path_act.split(separator)[:-1])
    return str(dir)
