# import pandas
import os
import time


def creation_time(filepath: str):
    """Recieve creation time of a file

    Args:
        filepath (str): path to csv-file

    Returns:
        time: Time the file was created
    """
    return time.ctime(os.path.getmtime(filepath))


print(creation_time(r"C:/Users/Datasets/marketing_campaign.csv"))


# df = pd.read_csv(r"C:/Users/Datasets/marketing_campaign.csv", delimiter=";")