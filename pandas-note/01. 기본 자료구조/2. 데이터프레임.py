import pandas as pd

data = {"name": ["Kim", "Lee", "Park"], "age": [24, 27, 34], "children": [2, 1, 3]}

df = pd.DataFrame(data=data, columns=[1, "학번", "성적"])
df.columns
df.dtypes
df.transpose()
