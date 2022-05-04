import numpy as np
import pandas as pd


def replace_missing_value(dataframe, value_types):

    for type in value_types:

        new_dataframe = dataframe.replace(type, np.nan)

    return new_dataframe


dict = {
    "column a": [0, 90, np.nan, 95],
    "column b": [30, 45, 56, 0],
    "column c": [np.nan, 40, 80, 98],
    "column d": [np.nan, 12, 35, None],
}

# creating a dataframe from list
df = pd.DataFrame(dict)

df = replace_missing_value(df, [np.nan, 0])

print(df)