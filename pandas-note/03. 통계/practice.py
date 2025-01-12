from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

df = sns.load_dataset("titanic")
df.head()

# 전반적인 주요 통계를 제공한다.
df.describe()

df.describe(include="object")

# 칼럼별로 행이 몇 개나 있는지
df.count()

df["survived"].count()

df.mean(numeric_only=True)

# 탑승자 평균 나이는 29.7살
# df["age"].mean()

# condition = df["adult_male"] == True
# df.loc[df["pclass"] == 2, "fare"].mean()

# df.mean(skipna=False)

pd.Series([1, 2, 3, 4, 5]).median()
