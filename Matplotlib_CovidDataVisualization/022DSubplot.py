 
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")

türkiye=df[df["Country/Region"]=="Turkey"]
italya=df[df["Country/Region"]=="Italy"]
ispanya=df[df["Country/Region"]=="Spain"]

df.plot(subplots=True)

plt.subplot(2,1,1)
plt.plot(ispanya.Deaths,ispanya.Recovered,color="blue",label="İspanyada ölen-iyileşen hasta sayıları")
plt.xlabel("İspanyadaki ölüm sayısı")
plt.ylabel("İspanyadaki iyileşen hasta sayısı")

plt.subplot(2,1,2)
plt.plot(italya.Deaths,italya.Recovered,color="black",label="italyada ölen-iyileşen hasta sayıları")
plt.xlabel("italya ölüm sayısı")
plt.ylabel("italya iyileşen hasta sayısı")

plt.show()