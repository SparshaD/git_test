
import pandas as pd

df = pd.read_csv('CarPrice.csv',nrows=100)

print(df.head())

print(df.iloc[:,2].value_counts())
