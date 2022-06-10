def degree_of_unambiguous(dataframe):

    sum_of_duplicates = dataframe.duplicated(subset=None, keep="first").sum()

    return ((dataframe.size - sum_of_duplicates) / dataframe.size) * 100
