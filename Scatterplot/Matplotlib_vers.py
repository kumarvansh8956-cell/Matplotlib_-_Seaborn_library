import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head())

print(df.columns)
da = df.loc[df["Seller Type"] == "Individual"]
den = df.loc[df["Seller Type"] == "Corporate"]
ma.scatter( x = da["Year"], y = da["Price"], label = "Individual")
ma.show()