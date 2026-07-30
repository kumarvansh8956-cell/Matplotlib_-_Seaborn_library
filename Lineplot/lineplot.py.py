import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head(10))
maxi = df.groupby("Make")['Price'].sum()
print(maxi.sort_values(ascending= False))
"""
 company Mercedes-Benz  has highest total price  749810995


"""
da = df.loc[df["Make"] == "Mercedes-Benz"]
print(da)
s.lineplot(data = da , x = da["Price"], y = da["Year"])
ma.title("Cars_price_by_the_Year")
ma.xlabel("Price")
ma.ylabel("year")
ma.show()