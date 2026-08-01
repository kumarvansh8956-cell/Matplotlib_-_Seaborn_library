import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head())

print(df.columns)

mak = df.groupby("Make")['Model'].count().sort_values(ascending=False).head(3)
print(mak)

Working_data = df.loc[df["Make"].isin(mak.index)]
print(Working_data)
ma.figure(figsize=(10,7))
s.boxplot(data = Working_data , x= "Price", y ="Make")
ma.show()