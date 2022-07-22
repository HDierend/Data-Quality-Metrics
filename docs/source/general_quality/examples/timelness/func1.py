# import pandas
import os
import time


print(time.ctime(os.path.getmtime(r"C:/Users/Datasets/marketing_campaign.csv")))

# df = pd.read_csv(r"C:/Users/Datasets/marketing_campaign.csv", delimiter=";")