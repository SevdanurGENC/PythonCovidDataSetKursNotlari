import pandas as pd

df=pd.read_csv("covid_19_data.csv")
print(df)

first=df["Province/State"]
print(first)

second=df[["Province/State","Country/Region"]]
print(second)

#loc(satır,sütun)
c1=df.loc[1]
print(c1)

c2=df.loc[1:55]
print(c2)

c3=df.loc[:,"Province/State"]
print(c3)

c4=df.loc[:,["Province/State","Country/Region"]]
print(c4)

c5=df.loc[3:45,["Province/State","Country/Region"]]
print(c5)

c6=df.iloc[5]
print(c6)

c7=df[df.Deaths<10]
print(c7)

c8=df[df.Recovered>55]
print(c8)