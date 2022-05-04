import numpy as np


def replace_missing_value(dataframe, value_types):

    for type in value_types:

        new_dataframe = dataframe.replace(type, np.nan)

    return new_dataframe
