import pandas as pd
import numpy as np
import time

date_data = {"2021-01-02": [1, 2], "2021-01-03": [3, 4], "2021-01-04": [5, 6]}
dateTable = pd.DataFrame(data=date_data)
print(dateTable)


# np.random.seed(int(time.time()))
# arr = np.random.randint(10, size=(2, 2))

# arr[0, 0] = 99

# df1 = pd.DataFrame(arr, copy=False)
# df2 = pd.DataFrame(arr, copy=True)
