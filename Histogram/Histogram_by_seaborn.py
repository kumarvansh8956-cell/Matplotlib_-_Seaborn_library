import matplotlib.pyplot as ma
import seaborn as s
import pandas as p

df = p.read_csv("car details v4.csv")
print(df.T.head(10))

data = df.groupby("Year")["Make"].count()                    
print(data)

s.histplot(data, bins = 10)
ma.show()