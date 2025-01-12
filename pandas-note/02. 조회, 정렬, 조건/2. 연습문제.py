from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

# 1. embark_town은 승객의 탑승 항구를 나타내는 column 입니다. 탑승 항구별 승객 데이터 분포를 확인해 주세요.
df.value_counts("embark_town")
df["embark_town"].value_counts()
df["embark_town"]


# 2.
# total_bill과 tip에 대한 내림차순 정렬을 해주세요
# 상위 10개만 출력하세요
tips = sns.load_dataset("tips")
tips.head()

tips.sort_values(["total_bill", "tip"], ascending=False).head(10)

# 3.
# size를 기준으로 내림차순, tip을 기준으로는 오름차순 정렬을 해주세요

tips.sort_values(["size", "tip"], ascending=[False, True])

# 4.
# 다음과 같은 결과를 가지도록 인덱싱 혹은 슬라이싱 하세요
df[3:8]

# 5.
#
df.loc[0:4, ["pclass", "sex", "age", "sibsp", "parch", "fare"]]

# 6.
#
df.loc[[i for i in range(2, 11, 2)], ["age", "who"]]


# 7.
# 나이가 30살 이상 남자 승객 조건 필터링
# fare를 많이 낸 순서로 내림차순 정렬
# 상위 10개를 출력


df = sns.load_dataset("titanic")
df.head()

df.loc[(df["sex"] == "male") & (df["age"] > 30)].sort_values(
    "fare", ascending=False
).head(10)


# 8.
# 나이가 20살 이상 40살 미만인 승객
# pclass가 1등급 혹은 2등급인 승객
# 열(column)은 survived, pclass, age, fare 만 나오게 출력
# 10개만 출력

df.loc[
    (~df["age"].isna())
    & (~df["pclass"].isna())
    & (df["age"] >= 20)
    & (df["age"] < 40)
    & (df["pclass"] == 1)
    | (df["pclass"] == 2),
    ["survived", "pclass", "age", "fare"],
].head(10)

df.loc[
    (~df["age"].isna())
    & (~df["pclass"].isna())
    & (
        (df["age"] >= 20) & (df["age"] < 40) & (df["pclass"] == 1) | (df["pclass"] == 2)
    ),
    ["survived", "pclass", "age", "fare"],
].head(10)


# 9.
# tips 데이터셋 중 day가 금요일(Fri), 토요일(Sat) 만 필터링 합니다.
# tip이 $10보다 적게 낸 데이터만 필터링합니다.
# 컬럼은 total_bill, tip, smoker, time만 출력합니다.
# 상위 10개 행만 출력합니다.

tips = sns.load_dataset("tips")
tips.head()


# isin() 함수를 사용하면 tips.loc[tips['day'].isin(['Sat', 'Fri'])] 처럼 작성할 수 있다.
tips.loc[
    ((tips["day"] == "Sat") | (tips["day"] == "Fri")) & (tips["tip"] < 10),
    ["total_bill", "tip", "smoker", "time"],
].head(10)

# To-Be
tips.loc[
    tips["day"].isin(["Sat", "Fri"]) & (tips["tip"] < 10),
    ["total_bill", "tip", "smoker", "time"],
].head(10)
