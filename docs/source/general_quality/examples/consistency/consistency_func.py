# importing pandas
import pandas as pd

# importing numpy
import numpy as np

# dictionary of lists
dict = {
    "column a": [0, 90, np.nan, "wort"],
    "column b": [30, 45, 56, 0],
    "column c": [np.nan, 40, 80, 98],
    "column d": [np.nan, 12, 35, None],
}

# creating a dataframe from list
df = pd.DataFrame(dict)

# define function to check for different datatypes
def check_for_types(dataframe):
    """_summary_

    Args:
        dataframe (_type_): _description_
    """
    for dtype, column in zip(dataframe.dtypes, dataframe.columns):
        if dtype == object:
            print(f'{column} contains multiple different datatypes!')

check_for_types(df)

