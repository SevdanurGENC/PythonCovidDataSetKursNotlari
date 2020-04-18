 

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")
"""
df.plot()
plt.show()

df=df.drop("SNo",axis=1)
df.plot()
plt.show()

türkiye=df[df["Country/Region"]=="Turkey"]
print(türkiye.columns)

plt.plot(türkiye.Deaths,türkiye.Recovered,color="red",label="Türkiyede ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("Türkiyedeki Coronavirüs analizi")
plt.legend()
plt.show()


italya=df[df["Country/Region"]=="Italy"]
plt.plot(italya.Deaths,italya.Recovered,color="blue",label="İtalyada ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("İtalyadaki Coronavirüs analizi")
plt.legend()
plt.show()
"""

ispanya=df[df["Country/Region"]=="Spain"]
plt.plot(ispanya.Deaths,ispanya.Recovered,color="yellow",label="ispanyada ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("İspanyadaki Coronavirüs analizi")
plt.legend()
plt.show()

df.plot(grid=True,linestyle=":")
plt.show()
















