import pandas as pd

df = pd.read_csv('data.csv')

df["name"].fillna('not-available', inplace = True) 
df["age"].fillna(25, inplace = True) 

print(df.to_string()) 
