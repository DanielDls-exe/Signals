import pandas as pd
from sklearn.model_selection import train_test_split

def generated_tts():
    df = pd.read_csv('dataset.csv')
    df.columns = [i for i in range(df.shape[1])]
    df = df.rename(columns={63: 'Output'})
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]
    return train_test_split(X, Y, test_size=0.2)
