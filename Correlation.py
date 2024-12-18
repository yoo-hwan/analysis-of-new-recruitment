## 2. 연도별(2019~2023) 일반정규직 채용 증가율과 청년고용증가율 에 따른 상관관계 (이전지역지역인재)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic') 
plt.rcParams['axes.unicode_minus'] = False  

recruitment_df = pd.read_excel('/Users/hwan/Desktop/충북대/5-2/빅데이터분석시각화/[finalproject]2020039093_유환/new_recruitment.xlsx')

target_items = ['일반정규직총신규채용', '이전지역지역인재', '고졸인력']
filtered_recruitment = recruitment_df[recruitment_df['항목'].isin(target_items)]

recruitment_totals = filtered_recruitment.groupby('항목')[['2019년', '2020년', '2021년', '2022년', '2023년']].sum().T
recruitment_totals.reset_index(inplace=True)
recruitment_totals.columns = ['연도', '일반정규직총신규채용', '이전지역지역인재', '고졸인력']
recruitment_totals['연도'] = recruitment_totals['연도'].str.replace('년', '').astype(int)

for col in ['일반정규직총신규채용', '이전지역지역인재', '고졸인력']:
    recruitment_totals[f'{col}_증가율'] = recruitment_totals[col].pct_change() * 100

employment_rate_df = pd.read_csv('/Users/hwan/Desktop/충북대/5-2/빅데이터분석시각화/[finalproject]2020039093_유환/employment_rate.csv', encoding='cp949')

filtered_employment_rate = employment_rate_df[(employment_rate_df['시도별'] == '계') & 
                                              (employment_rate_df['연령계층별'] == '15 - 29세')]

employment_rates = filtered_employment_rate[['2019', '2020', '2021', '2022', '2023']].T.reset_index()
employment_rates.columns = ['연도', '고용률']
employment_rates['연도'] = employment_rates['연도'].astype(int)
employment_rates['고용률_증가율'] = employment_rates['고용률'].pct_change() * 100

merged_data = pd.merge(recruitment_totals[['연도', '일반정규직총신규채용_증가율', '이전지역지역인재_증가율', '고졸인력_증가율']],
                       employment_rates[['연도', '고용률_증가율']],
                       on='연도').dropna() 

correlation_matrix = merged_data[['일반정규직총신규채용_증가율', '이전지역지역인재_증가율', '고졸인력_증가율', '고용률_증가율']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, fmt='.2f', square=True)
plt.title('채용 증가율과 고용률 증가율 간 상관관계')
plt.xticks(ticks=[0.5, 1.5, 2.5, 3.5], labels=['일반정규직 증가율', '이전지역 인재 증가율', '고졸인력 증가율', '고용률 증가율'], rotation=45)
plt.yticks(ticks=[0.5, 1.5, 2.5, 3.5], labels=['일반정규직 증가율', '이전지역 인재 증가율', '고졸인력 증가율', '고용률 증가율'], rotation=0)
plt.tight_layout()
plt.show()
