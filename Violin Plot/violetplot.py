import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.columns)

Max = df.groupby("Make")["Price"].sum().sort_values(ascending= False).head(3)
print(Max)
Mak_data =df.loc[df["Make"].isin(Max.index)]
print(Mak_data)

# A Violin Plot combines a Box Plot and a Kernel Density Estimate (KDE) to show both the distribution and summary statistics of numerical data.

"""
t displays:

Median
Quartiles
Data distribution (density)
Spread of the data

Best used when: Comparing the distribution of a numerical variable across different categories.

"""
s.violinplot(data=Mak_data, x="Make", y="Price")
ma.show()