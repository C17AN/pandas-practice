import pandas as pd

data = [[1, 10, 100], [2, 20, 200], [3, 30, 300]]
data2 = [[4, 40, 400], [5, 50, 500], [6, 60, 600]]
data3 = [[1], [2], [3, 4]]

df = pd.DataFrame(
    data=data, index=["row 1", "row 2", "row 3"], columns=["col 1", "col 2", "col 3"]
)

df2 = pd.DataFrame(
    data=data2, index=["row 1", "row 2", "row 3"], columns=["col 1", "col 2", "col 3"]
)

df3 = pd.DataFrame(
    data=data3, index=["row 1", "row 2", "row 3"], columns=["col 1", "col 2"]
)

df.sub(df3, fill_value=0)
