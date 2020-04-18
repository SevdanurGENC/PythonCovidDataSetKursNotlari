import pandas as pd

df=pd.read_csv("covid_19_data.csv")
print(df)

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.head(10))

print(df.tail(10))

print(df.info())

print(df.isnull().sum())

print(df.describe())

print(df["Province/State"].describe())

a=(df.describe(include=["O"]))
print(a) 

b=(df["Country/Region"].value_counts())
print(b)

print(df[df["Province/State"]=="Chicago"])