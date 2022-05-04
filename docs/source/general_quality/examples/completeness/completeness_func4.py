def complete_data_series(dataframe):

    row_count_missing_data = dataframe.isnull().any(axis=1).sum()

    row_count = len(dataframe)

    return 1 - (row_count_missing_data / row_count)
