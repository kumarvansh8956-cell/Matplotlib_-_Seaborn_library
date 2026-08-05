import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.columns)

Max = df.groupby("Make")["Price"].sum().sort_values(ascending= False).head(3)
print(Max)
Mak_data =df.loc[df["Make"].isin(Max.index)]
print(Mak_data)
s.violinplot(data=Mak_data, x="Make", y="Price", order=[ "Audi", "Mercedes-Benz","BMW"], linewidth= 1.6, linecolor= "red",inner="stick")
"""


Order :- its use to arrange the order
linewidth :- set the line width, it range is between 1 to 2
linecolor :- set the color of the line
inner :- it controls what statistical information or data points are displayed inside the violin plot, such as a box plot, quartile lines, points, sticks, or nothing.

"""
ma.show()