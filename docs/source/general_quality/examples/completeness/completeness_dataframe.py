# importing pandas as pd
import pandas as pd

# importing numpy as np
import numpy as np

# dictionary of lists
dict = {
    "column a": [100, 90, np.nan, 95],
    "column b": [30, 45, 56, None],
    "column c": [np.nan, 40, 80, 98],
    "column d": [np.nan, 40, 80, None],
}

# creating a dataframe from list
df = pd.DataFrame(dict)
