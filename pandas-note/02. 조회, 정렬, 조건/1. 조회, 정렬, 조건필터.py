from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.info()
df.sort_values(by=["fare", "age"], ascending=[False, True]).head()

df.loc[5]
df.loc[5, "class"]
df.loc[2:5, ["age"]]

df.head()
df
