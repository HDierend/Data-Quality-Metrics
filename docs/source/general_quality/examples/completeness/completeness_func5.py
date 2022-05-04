# importing pandas as pd
import pandas as pd


def degree_of_completeness(dataframe):

    entrie_count = dataframe.size

    missing_data_count = dataframe.isnull().sum().sum()

    return 1 - (missing_data_count / entrie_count)
