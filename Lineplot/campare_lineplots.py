import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head(10))

print(df.columns)
maxi = df.groupby("Seller Type")['Price'].sum()
print(maxi.sort_values(ascending= False))
da = df.loc[df["Seller Type"] == "Individual"]
den = df.loc[df["Seller Type"] == "Corporate"]
s.lineplot(data = da , x = da["Year"], y = da["Price"], label = "Individual")
s.lineplot(data = den , x = den["Year"], y = den["Price"], label = "Corporate")
ma.legend(loc=(0.5,0.5))
ma.title("Individual sells vs Corporate sells Years bias")
ma.xlabel("Price")
ma.ylabel("year")
ma.show()