import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.columns)

Max = df.groupby("Make")["Price"].sum().sort_values(ascending= False).head(3)
print(Max)
Mak_data =df.loc[df["Make"].isin(Max.index)]
print(Mak_data)
ma.violinplot(Mak_data["Price"])
ma.show()