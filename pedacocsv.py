import pandas as pd
df = pd.read_csv('imu_COVID_RJ_prepared.csv')
print(df.h)
print(df.head(5))
print(df.columns)
print(df.info())    