## 3. 연도별(2019~2023) 공기업,준정부기관,기타공공기관별 신입사원연봉 히스토그램 

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

rc('font', family='AppleGothic') 
plt.rcParams['axes.unicode_minus'] = False

salary_df = pd.read_excel('/Users/hwan/Desktop/충북대/5-2/빅데이터분석시각화/[finalproject]2020039093_유환/salary.xlsx') 

filtered_df = salary_df[salary_df['항목'] == '합계']

valid_institutions = ['공기업(시장형)', '공기업(준시장형)', '준정부기관(기금관리형)', '준정부기관(위탁집행형)','기타공공기관']
filtered_df = filtered_df[filtered_df['기관유형'].isin(valid_institutions)]

years = ['2019년', '2020년', '2021년', '2022년', '2023년']

salary_by_year_institution = filtered_df.melt(id_vars=['기관유형'], value_vars=years, var_name='연도', value_name='금액')
salary_by_year_institution['금액'] = pd.to_numeric(salary_by_year_institution['금액'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.barplot(
    data=salary_by_year_institution,
    x='연도',
    y='금액',
    hue='기관유형',
    hue_order=['공기업(시장형)', '공기업(준시장형)', '준정부기관(기금관리형)', '준정부기관(위탁집행형)', '기타공공기관'],
    palette='Set2'
)

plt.title('연도별 기관유형 금액 분포')
plt.xlabel('연도')
plt.ylabel('금액(천원)')
plt.tight_layout()
plt.show()
