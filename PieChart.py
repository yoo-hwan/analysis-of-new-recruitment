## 1. 연도별(2019~2023) 일반정규직, 지역인재, 고졸 채용율 파이차트

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc

new_recruitment_df = pd.read_excel('/Users/hwan/Desktop/충북대/5-2/빅데이터분석시각화/[finalproject]2020039093_유환/new_recruitment.xlsx')

data = new_recruitment_df[['기관명', '항목', '2019년', '2020년', '2021년', '2022년', '2023년']]

rc('font', family='AppleGothic') 
plt.rcParams['axes.unicode_minus'] = False  

target_items = ['일반정규직총신규채용', '이전지역지역인재', '고졸인력']
filtered_data = data.copy()
filtered_data['항목'] = filtered_data['항목'].apply(lambda x: x if x in target_items else '기타')

years = ['2019년', '2020년', '2021년', '2022년', '2023년']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for i, year in enumerate(years):
    year_data = filtered_data[['항목', year]].groupby('항목').sum().reset_index()

    ax = axes[i // 3, i % 3]
    ax.pie(
        year_data[year], 
        labels=year_data['항목'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('pastel')
    )
    ax.set_title(f"{year} 채용 비율")

axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
