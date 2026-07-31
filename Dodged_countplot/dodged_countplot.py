import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.head())

print(df.columns)

data = df[['Make','Seller Type']]
print(data)
mak = df.groupby("Make")['Model'].count().sort_values(ascending=False).head(3)
print(mak)
# Dodged Countplot: A countplot in which bars for different hue categories are displayed side by side for easy comparison.
Working_data = data.loc[data["Make"].isin(mak.index)]
print(Working_data)
ma.figure(figsize=(10,7))
s.countplot(data = Working_data , x= "Seller Type", hue="Make")
"""
          or
s.countplot(data = Working_data , x= "Seller Type", hue="Make", dodge = True)
because 
dodge =  True (default)

"""
ma.show()
"""
Use Dodged Countplot when:
  Comparing Male vs Female purchases.
  Comparing departments.
  Comparing product categories.

"""