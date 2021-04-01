import pandas as pd
df = pd.read_csv('../data/Meteorite_Landings.csv')
df.head(10) #View first 10 data rows
df.describe()
df.info()
