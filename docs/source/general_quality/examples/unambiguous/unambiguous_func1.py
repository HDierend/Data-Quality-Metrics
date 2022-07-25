# import pandas
import pandas as pd

# load dataset
df = pd.read_csv(r"C:/Users/Datasets/marketing_campaign.csv", delimiter=";")


def find_ambiguous_sets(dataframe, list_of_columns=None):

    return dataframe[dataframe.duplicated(list_of_columns, keep="first")]


def degree_of_unambiguous(dataframe):

    sum_of_duplicates = dataframe.duplicated(subset=None, keep="first").sum()

    return ((dataframe.size - sum_of_duplicates) / dataframe.size) * 100
