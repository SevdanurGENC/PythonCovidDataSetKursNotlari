import pandas as pd

sayılar=[0,1,2,3,4,5,6,7,8,9]
seriler=pd.Series(data=sayılar)

print(seriler.sum())

print(seriler.min())

print(seriler.max())

print(seriler.mean())

print(seriler.median())

print(seriler.var())

print(seriler.std())

sayılar2=[9,8,7,6,5,4,3,2,1,0]
seriler2=pd.Series(data=sayılar2)

print(seriler+seriler2)
print(seriler+5)
print(seriler-seriler2)
print(seriler*seriler2)
print(seriler*3)
print(seriler/seriler2)