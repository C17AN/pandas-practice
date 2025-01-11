import pandas as pd
import numpy as np

pd.Series([3, 5, 7, 9, 11], dtype="float32")


pd.Series(["가", "나", "다", "라", "마"], dtype="object")


sample = pd.Series(
    [10, 20, 30, 40, 50], index=["가", "나", "다", "라", "마"], dtype="int64"
)
sample.loc[["나", "라"]]

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)))
sample2[sample2 <= 160]
sample2[(sample2 >= 130) & (sample2 <= 170)]

pd.Series(data=["apple", "NaN", "banana"], index=["가", "나", "다"])

sample = pd.Series(["IT서비스", np.nan, "반도체", np.nan, "바이오", "자율주행"])
sample[sample.isnull()]


np.random.seed(0)
sample = pd.Series(np.random.randint(100, 200, size=(10,)))
sample[2:7]

np.random.seed(0)
sample2 = pd.Series(
    np.random.randint(100, 200, size=(10,)), index=list("가나다라마바사아자차")
)
sample2["바":"차"]

sample = pd.Series(data=["apple", "NaN", "banana"], index=["가", "나", "다"])
sample["가"]
