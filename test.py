import pandas as pd
import numpy as np
from numpy import nan

path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
mpg_data = pd.read_csv(path, delim_whitespace=True, header=None)
mpg_data.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']


def observations_and_features(dataset):
    """
    Returns the number of observations and features in the provided dataset
    """
    observations = dataset.shape[0]
    features = dataset.shape[1]

    return f"{observations} observations on {features} features".format(observations, features)

mpg_data.horsepower = mpg_data.horsepower.replace('?', np.nan)
mpg_data['horsepower'] = mpg_data['horsepower'].astype(float)
mpg_data_series = mpg_data['horsepower'].unique()


def get_unknown_hp(dataframe):
    """
    Returns the rows in the provided dataframe where the "horsepower" column is NaN
    """
    unknown_hp = []
    for row in mpg_data.horsepower:
        if row.isnull():
            unknown_hp.append(row)

    return unknown_hp

get_unknown_hp(mpg_data)