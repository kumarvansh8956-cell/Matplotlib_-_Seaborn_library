
import matplotlib.pyplot as ma
import pandas as p

df = p.read_csv("car details v4.csv")
print(df)

dat = df["Make"].value_counts().head()
print(dat)

ma.pie(dat,labels= dat.index, explode=(0.1,0,0,0,0,) ,autopct="%1.1f%%")
ma.show()