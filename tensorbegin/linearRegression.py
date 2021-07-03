import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.conf import settings

def loadDataset(file):
    df_train = pd.read_csv(settings.MEDIA_ROOT + '/' + file)
    df_eval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
    y_train = df_train.pop('survived')
    y_eval = df_eval.pop('survived')
    return df_train.head()