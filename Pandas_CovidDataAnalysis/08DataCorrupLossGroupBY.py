import pandas as pd
df=pd.read_csv("covid_19_data.csv")

a1=df.sort_values(by='Deaths',ascending=False).head(20)
print(a1)

df.drop(12969)
print(a1)

df=df.drop(12969)
print(df.sort_values(by='Deaths',ascending=False).head(20))

df.drop(12649,inplace=True)
print(df.sort_values(by='Deaths',ascending=False).head(20))
"""
df=df.drop("SNo",axis=1)
print(df.sort_values(by='Deaths',ascending=False).head(20))
"""
df=df.drop(columns="SNo")
print(df.columns)

print(df.groupby("Province/State")["Deaths"].mean().head(10))
print(df.groupby("Province/State")["Deaths"].max().head(10))

print(df.groupby(["Province/State","Country/Region"])["Deaths"].max().head(10))

print(df.isnull().sum())

df["Province/State"].fillna(method="ffill",inplace=True)

print(df.isnull().sum())

#df=df.drop() 

