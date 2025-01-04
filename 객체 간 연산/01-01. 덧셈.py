import pandas as pd


data = [[1, 10, 20], [2, 20, 200], [3, 30, 300]]
col = ["col1", "col2", "col3"]
row = ["row1", "row2", "row3"]

df = pd.DataFrame(data=data, index=row, columns=col)
# print(df)

# result = df.add(1)
# print(result)

data2 = [[2], [3], [4]]
df2 = pd.DataFrame(data=data2, index=row, columns=["col1"])

result = df.add(df2, fill_value=0)
print(result)
