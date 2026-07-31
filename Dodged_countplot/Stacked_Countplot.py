import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head())

print(df.columns)

data = df[['Make','Seller Type']]
print(data)
mak = df.groupby("Make")['Model'].count().sort_values(ascending=False).head(3)
# dodge=False → stacked/overlapped appearance instead of side-by-side bars
print(mak)

Working_data = data.loc[data["Make"].isin(mak.index)]
print(Working_data)
ma.figure(figsize=(10,7))

s.countplot(data = Working_data , x= "Seller Type", hue="Make", dodge = False)

ma.show()

"""
This is also know as Stacked countplot because all bars stack togather into one

"""