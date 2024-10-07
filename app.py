import pandas as pd

df = pd.read_csv('data.csv')

df.fillna({'name': 'not-avaialble'}, inplace = True) 
df.fillna({'age': 25}, inplace = True) 
df.fillna({'joining_dt': "2019/05/07"}, inplace = True) 

#df['joining_dt'] = pd.to_datetime(df['joining_dt'], 'coerce', format='yyyymmdd')

age_mean = df['age'].mean();
age_median = df['age'].median()

print(df.to_string()) 

print(f'mean age  is {age_mean} and median age is {age_median}') 
