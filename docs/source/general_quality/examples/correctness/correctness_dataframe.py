# import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv(r"C:/Users/Goerner/Desktop/beachwater.csv", delimiter=";")


plt.figure(figsize=(16, 5))
plt.subplot(1, 1, 1)
sns.distplot(df["Water Temperature"])
plt.show()

print(
    "Highest allowed",
    df["Water Temperature"].mean() + 3 * df["Water Temperature"].std(),
)
print(
    "Lowest allowed", df["Water Temperature"].mean() - 3 * df["Water Temperature"].std()
)
